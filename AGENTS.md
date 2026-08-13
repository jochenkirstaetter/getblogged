# GhostFx - Agent & Developer Workflow Guide

This document outlines the architecture, build instructions, and testing workflows for the `ghostfx` blog project.

---

## Overview & Project Structure

- **Framework**: DocFX static site generator.
- **Site Configuration**: [`posts/docfx.json`](posts/docfx.json)
- **Active Template**: [`posts/ghostfx/`](posts/ghostfx/)
- **Hosting Config**: [`firebase.json`](firebase.json)
- **Build Output**: `posts/_site/` (generated static HTML, assets, and metadata)

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

---

## Build & Test Workflow

### 1. Build the Site

To compile all markdown posts, conceptual documents, and assets into `posts/_site/`:

```bash
docfx build posts/docfx.json
```

Verify that the build succeeds with `0 warning(s)` and `0 error(s)`.

---

### 2. Run Local Server

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

---

## Verification & Quality Checks

When testing changes locally:
1. **Console & Runtime**: Open DevTools on `http://localhost:5000` and check for JavaScript errors or broken resources.
2. **Service Worker**: Verify `sw-v1.js` registers properly and outputs:
   `"Assets cached by the controlling service worker."`
3. **Syntax Highlighting**: Verify code snippets are highlighted using Highlight.js (`v11.11.1`).
4. **Google Analytics**: Confirm the GA4 Measurement tag (`G-F1KD1511QR`) is populated in the page header from `posts/docfx.json`.
5. **Hard Refresh**: When updating templates or scripts, perform a hard refresh or unregister the Service Worker in DevTools (`Application` > `Service Workers` > `Unregister`) to clear local caching.
