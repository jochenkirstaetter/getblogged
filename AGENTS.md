# GhostFx - Agent & Developer Workflow Guide

This document outlines the architecture, build instructions, pre/post-actions, testing workflows, and deployment processes for the `ghostfx` blog project.

---

## Overview & Project Structure

- **Framework**: DocFX static site generator.
- **Site Configuration**: [`posts/docfx.json`](posts/docfx.json)
- **Active Template**: [`posts/ghostfx/`](posts/ghostfx/)
- **Hosting Config**: [`firebase.json`](firebase.json)
- **Build Output**: `posts/_site/` (generated static HTML, assets, and metadata)
- **Raw Markdown Output**: `posts/_site/raw/` (frontmatter-stripped Markdown source files)

---

## Prerequisites

- **.NET SDK & DocFX Tool**:
  ```bash
  dotnet tool install -g docfx
  ```
- **Firebase CLI** (for local hosting emulation & deployment):
  ```bash
  npm install -g firebase-tools
  ```
- **Python 3** (for pre- and post-build automation scripts):
  ```bash
  python3 --version
  ```

---

## Complete Build & Deployment Pipeline

### Stage 1: Pre-Actions (Content & Asset Preparation)

Run these scripts when authoring new posts, optimizing assets, or cleaning content:

1. **Asset Localization & WebP Generation**:
   ```bash
   python3 scripts/localize-assets.py
   ```
   - Downloads remote Unsplash and CDN assets.
   - Generates responsive WebP images in `posts/content/images/`.
   - Normalizes image paths across markdown posts.

2. **Code Snippet HTML Entity Sanitization**:
   ```bash
   python3 scripts/fix-html-entities-in-code.py
   ```
   - Decodes HTML entities (e.g. `&nbsp;`, `&lt;`, `&amp;`, `&quot;`) inside code fences and inline backticks.

---

### Stage 2: Site Build (DocFX Compilation)

Compile all markdown posts, conceptual documents, and assets into `posts/_site/`:

```bash
docfx build posts/docfx.json
```

> [!IMPORTANT]
> Verify that the build completes with **`0 warning(s)`** and **`0 error(s)`**.

---

### Stage 3: Post-Actions (Markdown Artifacts Generation)

Generate frontmatter-free Markdown source files used by the viewer modal, copy buttons, and direct downloads:

```bash
python3 scripts/generate-clean-markdown.py
```

- Strips DocFX YAML frontmatter headers from `posts/published/` and `posts/pages/`.
- Outputs clean Markdown files into `posts/_site/raw/<slug>.md`.

---

### Stage 4: Local Preview & Quality Verification

#### Option A: Firebase Emulator (Recommended)
Simulates the production Firebase Hosting environment with redirects, rewrites, and clean URLs:

```bash
firebase emulators:start
```
- **Local URL**: `http://localhost:5000`
- **Hosting Target**: `posts/_site/`

#### Option B: DocFX Built-in Server
Quick local preview directly from DocFX:

```bash
docfx build posts/docfx.json --serve
```
- **Local URL**: `http://localhost:8080`

#### Verification Checklist
When testing changes locally on `http://localhost:5000`:
1. **Console & Runtime**: Open DevTools and verify 0 JavaScript errors or 404 broken resources.
2. **Search Palette**: Press `Ctrl+K` (or click search in nav) and verify fuzzy search indexing and keyboard navigation.
3. **Markdown Viewer & Copy**: Test `[ Copy Markdown ]` and `[ View Markdown ]` modal popups and download links.
4. **Service Worker**: Verify `sw-v1.js` registers properly and outputs:
   `"Assets cached by the controlling service worker."`
5. **Syntax Highlighting**: Verify code snippets and custom syntax (e.g. VFP) are highlighted with Highlight.js (`v11.11.1`).
6. **Google Analytics**: Confirm the GA4 Measurement tag (`G-F1KD1511QR`) is populated in the page header from `posts/docfx.json`.
7. **Hard Refresh**: When updating templates or scripts, unregister the Service Worker in DevTools (`Application` > `Service Workers` > `Unregister`) or perform a hard refresh to bypass caching.

---

### Stage 5: Deployment (Firebase Hosting)

#### Preview Channel (Staging)
To deploy a temporary preview channel for review:

```bash
firebase hosting:channel:deploy <channel-name>
```

#### Production Deployment
To deploy the static site to production (`jochen.kirstaetter.name` / `getblogged-b8929`):

```bash
# 1. Full build & post-processing
docfx build posts/docfx.json && python3 scripts/generate-clean-markdown.py

# 2. Deploy to Firebase Hosting
firebase deploy --only hosting
```
