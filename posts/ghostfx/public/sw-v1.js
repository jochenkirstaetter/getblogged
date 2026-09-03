'use strict';

/**
 * GhostFx Modern Service Worker
 * Standalone PWA offline caching without legacy external dependencies.
 */

const CACHE_NAME_STATIC = 'ghostfx-static-v125-e43230f';
const CACHE_NAME_CONTENT = 'ghostfx-content-v125-e43230f';

// Domains that should always bypass service worker caching
const BYPASS_ORIGINS = [
  'disqus.com',
  'disquscdn.com',
  'www.google-analytics.com',
  'www.googletagmanager.com',
  'pagead2.googlesyndication.com'
];

self.addEventListener('install', (event) => {
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys
          .filter((key) => key !== CACHE_NAME_STATIC && key !== CACHE_NAME_CONTENT)
          .map((key) => caches.delete(key))
      );
    }).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const request = event.request;

  // Only handle GET requests
  if (request.method !== 'GET') return;

  const url = new URL(request.url);

  // Bypass specific external third-party origins
  if (BYPASS_ORIGINS.some((domain) => url.hostname.includes(domain))) {
    return;
  }

  // Stale-While-Revalidate for static assets (local public/assets or external fonts)
  const isStaticAsset =
    url.pathname.startsWith('/public/') ||
    url.pathname.startsWith('/assets/') ||
    url.pathname.startsWith('/content/') ||
    url.hostname.includes('fonts.googleapis.com') ||
    url.hostname.includes('fonts.gstatic.com') ||
    url.hostname.includes('cdnjs.cloudflare.com') ||
    /\.(css|js|png|jpg|jpeg|gif|svg|ico|woff|woff2|ttf|eot)$/i.test(url.pathname);

  if (isStaticAsset) {
    event.respondWith(
      caches.open(CACHE_NAME_STATIC).then((cache) => {
        return cache.match(request).then((cachedResponse) => {
          const fetchPromise = fetch(request)
            .then((networkResponse) => {
              if (networkResponse && networkResponse.status === 200) {
                cache.put(request, networkResponse.clone());
              }
              return networkResponse;
            })
            .catch(() => cachedResponse);

          return cachedResponse || fetchPromise;
        });
      })
    );
    return;
  }

  // Network-First for HTML content pages (with cache fallback for offline reading)
  const isHtmlNavigation =
    request.mode === 'navigate' ||
    (request.headers.get('accept') && request.headers.get('accept').includes('text/html'));

  if (isHtmlNavigation) {
    event.respondWith(
      fetch(request)
        .then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200) {
            const responseClone = networkResponse.clone();
            caches.open(CACHE_NAME_CONTENT).then((cache) => {
              cache.put(request, responseClone);
            });
          }
          return networkResponse;
        })
        .catch(() => caches.match(request))
    );
    return;
  }
});
