# GhostFx - Agent & Developer Workflow Guide

This document outlines the architecture, build instructions, pre/post-actions, testing workflows, and deployment processes for the `ghostfx` blog project.

---

## Overview & Project Structure

> [!NOTE]
> **GhostFx vs. `ghostfx` Terminology**:
> - **GhostFx**: The open-source static site converter project and ecosystem bridging Ghost themes with DocFX ([`jochenkirstaetter/ghostfx`](https://github.com/jochenkirstaetter/ghostfx)).
> - **`ghostfx`**: The active DocFX template folder ([`posts/ghostfx/`](posts/ghostfx/)) and local theme asset pipeline powering this blog.

- **Framework**: DocFX static site generator.
- **Production Site Configuration**: [`posts/docfx.json`](posts/docfx.json)
- **Draft Site Configuration**: [`posts/docfx.draft.json`](posts/docfx.draft.json) (includes `posts/draft/` content)
- **Draft Assets & Research**: `posts/draft/assets/<uid>/` (isolated workspace per draft for research notes, downloaded resources, and reference tracking)
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

## Agent Network & Web Requests

> [!IMPORTANT]
> For any web requests you must make with `curl` or otherwise, always set your user agent string to be `"OpenAI File Downloader, XaiImageApiFetch/1.0"`.

---

## Complete Build & Deployment Pipeline

### Stage 1: Pre-Actions (Content & Asset Preparation)

Run these scripts when authoring new posts, optimizing assets, or cleaning content:

1. **Asset Localization, WebP & Open Graph Generation**:
   ```bash
   python3 scripts/localize-assets.py
   ```
   - Downloads remote Unsplash and CDN assets.
   - Generates responsive WebP images in `posts/content/images/`.
   - Generates intelligent 1200×630 Open Graph preview cards (`<slug>-og.webp`) with hero backdrop, 42% frosted-glass plates, and extension-less QR code cards (preserving manual author overrides).
   - Normalizes image paths and `ogImage` frontmatter across markdown posts.

2. **Code Snippet HTML Entity Sanitization**:
   ```bash
   python3 scripts/fix-html-entities-in-code.py
   ```
   - Decodes HTML entities (e.g. `&nbsp;`, `&lt;`, `&amp;`, `&quot;`) inside code fences and inline backticks.

3. **Tag Index & Tag Pages Generation**:
   ```bash
   python3 scripts/generate-tags.py
   ```
   - Aggregates frontmatter tags across all published posts.
   - Generates `posts/tags.md` sorted alphabetically with exact published post counts.
   - Generates/updates individual tag detail pages in `posts/tags/<slug>.md` and `posts/tags/toc.yml`.

4. **Published Index Generation**:
   ```bash
   python3 scripts/generate-index.py
   ```
   - Aggregates published posts sorted in reverse chronological order.
   - Generates `posts/index.md` containing the top posts matching `_indexCount` configured in `posts/docfx.json`.

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

> [!IMPORTANT]
> **Mandatory User Approval Guardrail**: **Never** execute any Firebase deployment (`firebase deploy`, `npm run deploy`, or `firebase hosting:channel:deploy`) without explicit approval from the user. All build verification and staging reviews must remain strictly local (`firebase emulators:start` or `npm run serve`) until explicitly approved.

#### Pre-deployment Guardrail & Asset Versioning

1. **Artifact Preservation & Archival**:
   Prior to committing and initiating deployment, all artifacts generated during research, drafting, design, and review (e.g. `implementation_plan.md`, `walkthrough.md`, `images_used.md`, reference notes `resources.md`, and working media) must be saved into the post's associated draft assets directory (`posts/draft/assets/<uid>/`). This preserves research lineage, architectural decisions, and visual assets for future editorial reference.

2. **Git Clean Status Enforcement**:
   Deployments enforce clean Git content status via `scripts/check-clean-posts.py` (wired into `predeploy` in `package.json`).
   It verifies that all changes and new assets in `posts/published/`, `posts/draft/`, `posts/pages/`, `posts/content/`, and `posts/index.md` are committed before `deploy` proceeds. Upon passing, it automatically derives the latest Git revision metadata (`v<rev-count>-<short-hash>`) and updates `_assetVersion` in `posts/docfx.json`, `posts/docfx.draft.json`, and the Service Worker cache names in `posts/ghostfx/public/sw-v1.js`.

#### Preview Channel (Staging / Draft Review)
To deploy a temporary preview channel for review (with draft content included) once explicitly approved:

```bash
# 1. Clean, draft build & post-processing
npm run build:draft

# 2. Deploy temporary preview channel (requires user approval)
firebase hosting:channel:deploy <channel-name>
```

#### Production Deployment
To deploy the static site to production (`jochen.kirstaetter.name` / `getblogged-b8929`) once explicitly approved:

```bash
# 1. Full clean, production build & deploy (with pre-deploy guardrail, requires user approval)
npm run deploy
```

---

## Content Authoring & Editorial Guidelines
 
For detailed writing instructions, tone of voice, orthography rules (British English, no-em-dashes, DRY frontmatter), research isolation (`posts/draft/assets/<uid>/`), and draft publishing workflows, refer to:

👉 [**`AUTHORING.md`**](AUTHORING.md)

### Content Designer: Multi-Image Presentation Decisions

When authoring or updating posts with adjacent images, the Content Designer selects from the following four presentation modes:

1. **Ungrouped / Stacked (Default)**: Use blank lines between images for full-width diagrams or sequential tutorial steps.
2. **Auto-Fit Responsive Grid (`image-grid` / `::: grid` / `> [!GRID]`)**: Place images back-to-back in the same paragraph (or wrap in `::: grid`) for 2–4 side-by-side screenshots or 3–6 speaker photos.
3. **Horizontal Scroll-Snap Strip (`::: strip` / `> [!STRIP]`)**: Wrap in `::: strip` for 4–10 book covers (e.g. `Recension` posts) and horizontal wizard sequences.
4. **Expandable Event Album / Lightbox Gallery (`::: gallery` / `> [!GALLERY]`)**: Wrap in `::: gallery` for 6–9+ photo event dumps (DevFest, MSCC, Summits) to avoid vertical scroll fatigue while allowing high-resolution inspection.



