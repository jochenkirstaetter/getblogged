# GhostFx - Agent & Developer Workflow Guide

This document outlines the architecture, build instructions, pre/post-actions, testing workflows, and deployment processes for the `ghostfx` blog project.

---

## Overview & Project Structure

- **Framework**: DocFX static site generator.
- **Production Site Configuration**: [`posts/docfx.json`](posts/docfx.json)
- **Draft Site Configuration**: [`posts/docfx.draft.json`](posts/docfx.draft.json) (includes `posts/draft/` content)
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

Always clean/purge previous build artifacts (`posts/_site/`) before compiling:

#### Option A: Production Build (Published Posts Only)
Compile published markdown posts, conceptual documents, and assets into `posts/_site/`:

```bash
rm -rf posts/_site && docfx build posts/docfx.json
```

#### Option B: Draft & Preview Build (Includes `posts/draft/`)
Compile draft posts, the draft landing page (`index-draft.md`), and published content for local review and staging preview channels:
```bash
rm -rf posts/_site && python3 scripts/generate-draft-index.py && docfx build posts/docfx.draft.json
```
> [!IMPORTANT]
> Verify that the build completes with **`0 warning(s)`** and **`0 error(s)`**.

---

### Stage 3: Post-Actions (Markdown Artifacts Generation)

Generate frontmatter-free Markdown source files used by the viewer modal, copy buttons, and direct downloads:

- **Production**:
  ```bash
  python3 scripts/generate-clean-markdown.py
  ```
- **Including Drafts**:
  ```bash
  python3 scripts/generate-clean-markdown.py --draft
  ```

- Strips DocFX YAML frontmatter headers from markdown files.
- Outputs clean Markdown files into `posts/_site/raw/<slug>.md`.

---

### Stage 4: Local Preview & Quality Verification

#### Option A: Firebase Emulator (Recommended)
Simulates the production Firebase Hosting environment with redirects, rewrites, and clean URLs.
Hosting parameters (port and public directory) are defined in [`firebase.json`](firebase.json) under `emulators.hosting.port` and `hosting.public`:

```bash
# Build drafts with index and start emulator
npm run build:draft
firebase emulators:start
```
- **Local URL**: `http://localhost:<port>` (Check `emulators.hosting.port` in [`firebase.json`](firebase.json), e.g. `http://localhost:5002`)
- **Hosting Target**: Configured via `hosting.public` in [`firebase.json`](firebase.json) (e.g. `posts/_site/`)

#### Option B: DocFX Built-in Server

- **Production Content**:
  ```bash
  npm run serve
  ```
- **Including Drafts**:
  ```bash
  npm run serve:draft
  ```
- **Local URL**: `http://localhost:8080`

When testing changes locally on the configured emulator URL (`http://localhost:<port>`):
1. **Console & Runtime**: Open DevTools and verify 0 JavaScript errors or 404 broken resources.
3. **Markdown Viewer & Copy**: Test `[ Copy Markdown ]` and `[ View Markdown ]` modal popups and download links.
4. **Service Worker**: Verify `sw-v1.js` registers properly and outputs:
   `"Assets cached by the controlling service worker."`
5. **Syntax Highlighting**: Verify code snippets and custom syntax (e.g. VFP) are highlighted with Highlight.js (`v11.11.1`).
6. **Google Analytics**: Confirm the GA4 Measurement tag (`G-F1KD1511QR`) is populated in the page header from `posts/docfx.json`.
7. **Hard Refresh**: When updating templates or scripts, unregister the Service Worker in DevTools (`Application` > `Service Workers` > `Unregister`) or perform a hard refresh to bypass caching.

---

### Stage 5: Deployment (Firebase Hosting)

#### Pre-deployment Guardrail
Deployments enforce clean Git content status via `scripts/check-clean-posts.py` (wired into `predeploy` in `package.json`).
It verifies that all changes and new assets in `posts/published/`, `posts/draft/`, `posts/pages/`, `posts/content/`, and `posts/index.md` are committed before `deploy` proceeds.

#### Preview Channel (Staging / Draft Review)
To deploy a temporary preview channel for review (with draft content included):

```bash
# 1. Clean, draft build & post-processing
npm run build:draft

# 2. Deploy temporary preview channel
firebase hosting:channel:deploy <channel-name>
```

To deploy the static site to production (`jochen.kirstaetter.name` / `getblogged-b8929`):

```bash
# 1. Full clean, production build & deploy (with pre-deploy guardrail)
npm run deploy
```

---

## Draft Authoring & Publication Workflow

When creating, drafting, and publishing new articles:

1. **Authoring Drafts**:
   - Create post markdown file in `posts/draft/<slug>.md`.
   - Set frontmatter flags:
     ```yaml
     status: draft
     isDraft: true
     ```
   - Store and link hero and content images under `posts/content/images/<YYYY>/<MM>/`.
2. **Reviewing Drafts Locally**:
   - Build with draft configuration:
     ```bash
     npm run build:draft
     firebase emulators:start
     ```
   - Open `http://localhost:<port>/` to review the draft landing page feed.
   - (Optional) Deploy to a staging channel via `firebase hosting:channel:deploy draft-<slug>`.
3. **Promoting Draft to Published**:
   - Move the markdown file from `posts/draft/<slug>.md` to `posts/published/<slug>.md`.
     ```yaml
     status: published
     publishedAt: YYYY-MM-DDTHH:MM:SSZ
     updatedAt: YYYY-MM-DDTHH:MM:SSZ
     ```
   - Run full production build and verification:
     ```bash
     npm run build
     ```

