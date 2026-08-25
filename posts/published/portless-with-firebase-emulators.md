---
uid: portless-with-firebase-emulators
title: Using portless with Firebase Hosting
date: 2026-08-21
status: published
type: post
description: A practical guide on combining portless local HTTPS reverse proxy with Firebase Hosting Emulators for frictionless local web development without memorizing port numbers.
tags:
  - Development
keywords: 'firebase emulators, portless, reverse proxy, localhost, local https, development server, firebase hosting'
image: content/images/2026/08/portless-with-firebase-emulators.webp
ogImage: content/images/2026/08/portless-with-firebase-emulators-og.webp
layout: post
bodyClass: post-template tag-development
postClass: post tag-development
isPost: true
isPage: false
isDraft: false
isScheduled: false
isTagPage: false
isTagsIndexPage: false
isAuthorPage: false
isHome: false
author: Jochen Kirstätter
authorTwitter: '@jkirstaetter'
authorFacebook: https://facebook.com/jochen.kirstaetter
authorImage: content/images/2018/10/JoKi_StAubin_100px.webp
authorSlug: joki
canonicalUrl: https://jochen.kirstaetter.name/portless-with-firebase-emulators/
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
publishedAt: 2026-08-21T20:00:00Z
updatedAt: 2026-08-21T20:00:00Z
---
# Using portless with Firebase emulators

When developing multiple web applications and microservices locally, managing local port numbers quickly becomes tedious. Switching between `localhost:3000`, `localhost:5000`, `localhost:8080`, and `localhost:9099` leads to port collisions, CORS friction, and cookie domain mismatches.

To solve this, **`portless`** - [hosted on GitHub](https://github.com/vercel-labs/portless) - provides local domains without port exposure; but with automatic SSL certificates (e.g., `https://myproject.localhost/`) mapping seamlessly to your local dev processes.

However, the main development stack targeted seems to be anything Node.js based and pairing `portless` with the **[Firebase Emulator Suite](https://firebase.google.com/docs/emulator-suite)** introduces unique challenges because of how Firebase orchestrates its networking and emulator processes.

## The Problem

Standard frontend dev servers (like Vite, Next.js, or Webpack Dev Server) usually take a dynamically injected `PORT` environment variable or command-line argument.

With Firebase Local Emulators:
1. **Multiple Co-existing Ports**: Firebase spins up several emulators simultaneously (Hosting on `5000`, Functions on `5001`, Firestore on `8080`, Auth on `9099`, and the Emulator UI on `4000`).
2. **Fixed Port Defaults**: The Firebase CLI does not automatically adapt its Hosting emulator port to arbitrary environment variables like `PORT=34567` provided by automatic reverse proxies.
3. **HTTP vs HTTPS**: Firebase Hosting emulator serves over plain HTTP (`http://127.0.0.1:5000`), but modern browser features, secure cookies, and third-party auth callbacks frequently require HTTPS.
4. **Multiple projects**: Running multiple projects requires different unique ports assigned, and humans get confused easily. Having a project-related domain as URL is a productivity booster. 

## Architectural Obstacles & Exploration

### Obstacle 1: The Injected `PORT` Fallacy
Many proxy wrappers rely on launching a child command and expecting the framework to read `process.env.PORT`:

```bash
# What portless typically does under the hood
PORT=49152 npm run dev
```

When running `firebase emulators:start`, Firebase **ignores** `process.env.PORT` and defaults to port `5000` (or the port explicitly specified under `"emulators"."hosting"."port"` in `firebase.json`).

### Obstacle 2: The Root vs. User Space Split & `routes.json` Desynchronization

`portless` relies on a two-tier architecture:
1. **The Reverse Proxy Daemon**: Needs to bind to privileged ports (`80` for HTTP and `443` for HTTPS), requiring root privileges (`sudo portless proxy` or a system daemon).
2. **The Developer CLI**: Runs in regular user space to launch child processes and register routes on demand (`portless`).

Under the hood, route registrations are stored in a state file called **`routes.json`**. Because of the separation between root and user space, two major issues arise:

#### 1. The Disconnected `routes.json` Path
When the proxy daemon runs as `root`, its `$HOME` is `/root/`, so it listens for route changes inside:
```text
/root/.portless/routes.json
```
Meanwhile, when the developer runs `portless` as an unprivileged user, the CLI writes new mappings to:
```text
$HOME/.portless/routes.json
```

The CLI reports success:
```text
✔ Registered route: iosltd.localhost -> 127.0.0.1:5000 in $HOME/.portless/routes.json
✔ Starting child process: firebase emulators:start --only hosting
```

However, navigating to `https://iosltd.localhost/` in the browser fails with a `502 Bad Gateway` or `404 Not Found`, and the root proxy daemon emits:

```text
[portless:proxy] [WARN] Incoming request for "https://iosltd.localhost/"
[portless:proxy] [ERROR] Hostname "iosltd.localhost" not found in active routes table (/root/.portless/routes.json)
[portless:proxy] [INFO] Loaded routes: 0 registered targets
```

#### 2. File Ownership & `EACCES` Permission Errors
If the daemon is started pointing directly to the user's directory without dropping privileges, it creates or overwrites `routes.json` owned by `root:root`. The next time you run `portless` without `sudo`, the command immediately crashes with:

```text
node:fs:585
  handleErrorFromBinding(ctx);
  ^

Error: EACCES: permission denied, open '$HOME/.portless/routes.json'
    at Object.openSync (node:fs:585:18)
    at Object.writeFileSync (node:fs:2334:35)
    at registerRoute (/usr/local/lib/node_modules/portless/lib/routes.js:42:8)
    at async start (/usr/local/lib/node_modules/portless/bin/cli.js:88:5) {
  errno: -13,
  syscall: 'open',
  code: 'EACCES',
  path: '$HOME/.portless/routes.json'
}
```

#### The Resolution
Explicitly synchronize the state directory across both root and user environments using `PORTLESS_STATE_DIR`, and ensure the directory has user-level write permissions:

```bash
# 1. Export in user environment (~/.bashrc or ~/.zshrc):
export PORTLESS_STATE_DIR="$HOME/.portless"

# 2. When starting the elevated proxy daemon, pass the user state directory:
sudo PORTLESS_STATE_DIR="$HOME/.portless" portless proxy

# 3. Ensure proper file ownership if root previously touched the file:
sudo chown -R $USER:$USER "$HOME/.portless"
```

---

### Obstacle 3: Startup Delays with Full Emulator Suite
Running `firebase emulators:start` without filtering launches Java-based emulators (Firestore, Pub/Sub, Storage) which takes several seconds. When `portless` probes the port before the Hosting emulator binds, it might report a connection timeout.

**Resolution**: Narrow the emulator scope for web hosting development:

```bash
firebase emulators:start --only hosting
```
## The Solution: Explicit Configuration

The cleanest approach is to define an explicit `"portless"` declaration in your project's `package.json` mapping the domain alias directly to Firebase Hosting's port (e.g. `5000` or custom port like `5002`), while delegating the startup to `npm run dev`. That's the default launch script in `portless`. But what if you don't have a `package.json` file? It won't hurt or damage your project (e.g. a static website) to create a lightweight one—it provides a standard place for dev scripts and local tooling.

### 1. `package.json` Configuration

Here's a sample configuration:

```json
{
    "name": "ios-website",
    "version": "2.0.1",
    "description": "IOS Indian Ocean Software Ltd. - Software Solutions from Mauritius",
    "scripts": {
        "dev": "firebase emulators:start --only hosting"
    },
    "portless": {
        "name": "iosltd",
        "appPort": 5000
    }
}
```

* Add the standard project metadata like `name`, `version`, and `description`.
* Add the `portless` configuration block:
  * **`portless.name`**: Assigns the local hostname `https://iosltd.localhost/`. If omitted, the top-level `name` value is used.
  * **`portless.appPort`**: Points the reverse proxy directly to the internal port of your Firebase emulator (`5000`, or whatever port is set in `firebase.json`).
* **`scripts.dev`**: Runs the Firebase Hosting emulator exclusively. This is the command `portless` runs automatically.

---

### 2. `firebase.json` Configuration

Here is the corresponding `firebase.json` configuration, configuring static hosting and emulator ports:

```json
{
  "hosting": {
    "public": "public",
    "cleanUrls": true,
    "trailingSlash": false,
    "ignore": [
      "firebase.json",
      "!**/.well-known/**",
      "**/.*",
      "**/node_modules/**"
    ]
  },
  "emulators": {
    "hosting": {
      "port": 5000
    },
    "ui": {
      "enabled": true
    },
    "singleProjectMode": true
  }
}
```

> [!TIP]
> Always ensure that `"portless"."appPort"` in `package.json` matches `"emulators"."hosting"."port"` in `firebase.json`.

## Running the Setup

### Starting the Dev Environment via Portless

Run the `portless` command from the root of your project:

```bash
portless
```

This minimal approach relies on the default launch behaviour of `portless` and uses the configuration in `package.json` as described above. `portless` will launch the proxy route and run `npm run dev` in the child process.

### Terminal Output

```text

portless

-- Proxy is running
-- getblogged.localhost (auto-resolves to 127.0.0.1)
-- Name "iosltd" (from portless.json)
-- Using port 5000 (fixed)

  -> https://iosltd.localhost

Running: PORT=5000 HOST=127.0.0.1 PORTLESS_URL=https://iosltd.localhost NODE_EXTRA_CA_CERTS="$HOME/.portless/ca.pem" npm run dev


> iosltd@2.0.1 dev
> firebase emulators:start --only hosting

i  emulators: Starting emulators: hosting
⚠  hub: emulator hub unable to start on port 4400, starting on 4401 instead.
⚠  logging: Logging Emulator unable to start on port 4500, starting on 4501 instead.
i  hosting[iosltd]: Serving hosting files from: posts/_site
✔  hosting[iosltd]: Local server: http://127.0.0.1:5000
⚠  emulators: The Emulator UI is not starting because none of the running emulators have a UI component.

┌─────────────────────────────────────────────────────────────┐
│ ✔  All emulators ready! It is now safe to connect your app. │
└─────────────────────────────────────────────────────────────┘

┌──────────┬────────────────┐
│ Emulator │ Host:Port      │
├──────────┼────────────────┤
│ Hosting  │ 127.0.0.1:5000 │
└──────────┴────────────────┘

✔  Proxy active at: https://iosltd.localhost/
```

## Verification & Testing

You can now `curl` or open your browser directly to the clean `.localhost` domain with TLS:

```bash
curl -k https://iosltd.localhost/
```

### Output

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IOS Indian Ocean Software Ltd.</title>
  ...
```

## Stopping and Restarting the Proxy (Applying Changes)

When you modify `routes.json`, change environment variables (`PORTLESS_STATE_DIR`), update certificates, or alter your project's port mapping, you need to cleanly stop the running `portless` reverse proxy daemon so the changes take effect.

### 1. Stopping the Proxy Daemon

If you started the proxy via `sudo portless proxy` or as a background service:

```bash
# Graceful stop via CLI
sudo portless stop

# Or terminate the proxy process directly
sudo pkill -f "portless proxy"
```

### 2. Ensuring Ports 80 & 443 are Released

If the proxy crashed or did not release ports cleanly, verify that no orphaned processes are occupying the privileged web ports:

```bash
sudo lsof -i :80 -i :443
```

To forcefully release the ports if needed:

```bash
sudo fuser -k 80/tcp 443/tcp
```

### 3. Clearing Stale Routes (Optional)

If old project mappings or stale ephemeral ports remain in your routes table, you can wipe the user-level routes file:

```bash
rm -f "$HOME/.portless/routes.json"
```

### 4. Restarting the Proxy with Synchronized State

Restart the proxy daemon passing the explicit user state directory:

```bash
sudo PORTLESS_STATE_DIR="$HOME/.portless" portless proxy
```

Terminal output confirming clean restart:

```text
[portless:proxy] Initializing reverse proxy on ports 80 (HTTP) and 443 (HTTPS)...
[portless:proxy] Watching state directory: $HOME/.portless
[portless:proxy] Loaded 0 active routes from $HOME/.portless/routes.json
✔ Proxy is running and listening for incoming localhost traffic.
```

## Summary of Key Takeaways

1. **Explicit `appPort`**: Because Firebase Hosting emulator binds to a specific configured port (default `5000`, or custom e.g. `5002`), declare `"portless": { "name": "<project>", "appPort": <port> }` in `package.json`.
2. **Speed Up Startup**: Use `--only hosting` in your `npm run dev` script to avoid launching unnecessary emulators and prevent proxy timeouts.
3. **Environment Alignment**: Set `PORTLESS_STATE_DIR="$HOME/.portless"` to ensure smooth inter-process routing between the privileged proxy daemon and user CLI sessions.
4. **Clean Restarts**: Use `sudo portless stop` or `sudo pkill -f "portless proxy"` followed by restarting with the explicit `PORTLESS_STATE_DIR` to reload altered configurations.

