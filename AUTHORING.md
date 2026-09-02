# GhostFx - Authoring, Tone & Editorial Style Guide

This guide establishes the editorial principles, writing style, orthography rules, and asset conventions for authoring blog posts on `getblogged`.

---

## 1. Editorial Persona, Tone & Voice

- **Developer-to-Developer & Pragmatic**: Write with practical, hands-on experience. Focus on real workflows, terminal commands, architecture, and actionable solutions rather than theoretical overviews.
- **Candid & Authentic**: Provide genuine technical assessments. Openly highlight quirks, workarounds, edge cases, and missing functionality alongside successes. Avoid marketing hype or artificial enthusiasm.
- **Conversational & Direct**: Engage the reader naturally from a first-person perspective.
- **Fluff-Free & Concise**: Keep prose tight, substantive, and clear.
  - **Prohibited Words/Phrases**:
    - Do **not** use `"Let's be honest..."`
    - Do **not** use `"basically"`
    - Do **not** use `"easily"`
    - Do **not** use `"just"`

---

## 2. Orthography & Language Rules

### British English (B.E.)
All articles must strictly follow British English conventions:
- **`-ise` Suffixes**: Use *categorise*, *organise*, *synthesise*, *prioritise*, *visualise*, *optimise*, *customise* (never `-ize`).
- **Standard Spelling**:
  - *colour*, *behaviour*, *neighbour*, *favour*
  - *centre*, *theatre*, *metre*
  - *defence*, *licence* (noun)
- **Programme vs Program**:
  - Use ***programme*** for events, initiatives, curriculums, challenges, or schedules (e.g. *Google Africa Developer Scholarship programme*, *accelerator programme*).
  - Use ***program*** only when referring to computer executable code or software applications.
- **Consonant Doubling**:
  - Use *signalled*, *travelling*, *modelled*, *initialled*.
- **GhostFx vs. `ghostfx` Nomenclature**:
  - Use PascalCase **GhostFx** when referencing the open-source project, converter, or repository ([`jochenkirstaetter/ghostfx`](https://github.com/jochenkirstaetter/ghostfx)).
  - Use lowercase monospace **`ghostfx`** when referring to the local DocFX template directory (`posts/ghostfx/`), template identifier (`"template": ["ghostfx"]`), or client asset bundle.

### Latin Abbreviations & Precision
- **`e.g.`** (*exempli gratia* - "for example"): Always retain both periods (`e.g.`, never `eg` or `eg.`). Follow with a comma or relevant punctuation when introducing lists or inline examples.
- **`i.e.`** (*id est* - "that is" / "in other words"): Always retain both periods (`i.e.`, never `ie` or `ie.`). Use strictly for clarification or restatement, not for giving examples.
- **`etc.`** (*et cetera* - "and so forth"): Always include the trailing period (`etc.`, never `etc` without period unless terminating a sentence). Avoid redundant combinations like *"and etc."* or trailing ellipsis (*"..., etc..."*).
- **`et al.`** (*et alii* - "and others"): Period on `al.` only (`et al.`).

### Punctuation & Typography
- **Strict No-Em-Dash Rule**: **Never** use em-dash characters (`—`). Use standard hyphens (` - ` or `--`), commas, colons, or semicolons instead.
- **Contractions & Quotes**: Use standard straight or curly single and double quotes consistently. Avoid awkward stacked quotes.

---

## 3. Article Structure & Flow

Every full-length article should follow a clean, readable narrative flow:

1. **Introductory Hook**: Open with an engaging, direct observation, thought experiment, or problem statement that immediately frames the core topic.
2. **Context & Social Grounding**: When referencing real-world inspiration, conferences, or social discussions, cite and embed real posts (e.g. posts on X, LinkedIn, or community questions) with accurate links and attribution.
3. **Clear Progression / Phased Roadmap**: Break down technical implementations into structured phases, steps, or tiers (*"Phase 1: Triage"*, *"Phase 2: Review"*, etc.).
4. **Visuals & Layout**:
   - Place responsive WebP images in `posts/content/images/<YYYY>/<MM>/`.
   - Always provide descriptive `alt` text and `title` attributes.
   - For screenshots accompanying step-by-step descriptions, use floated layout (`float: right; margin: 0 0 1.5rem 1.5rem; max-width: 300px; width: 100%; border-radius: 8px;`) with a clearing `div` when appropriate.
   - For multi-image sets (2 to 9+ images), adhere to the **Image Presentation Options & Decision Framework** in Section 4 below.
5. **Technical Quirks & Missing Functionality**: Dedicate a section to friction points, platform-specific differences (e.g. Linux desktop vs macOS, CLI vs GUI), or feature gaps when reviewing new tools.
6. **Key Takeaways & References**: Provide a concise summary and link directly to official documentation, tools, or repos.
7. **Join the Conversation (CTA)**: Conclude with a warm, signature prompt inviting readers to connect and discuss on social platforms (X: `@JKirstaetter`, BlueSky: `@jochen.kirstaetter.name`, Mastodon: `@JKirstaetter`, RSS feed).
8. **Picture Credits & Attribution**: Include a footer credit line for AI-generated visuals or photography (e.g. `<small>Picture credits: ...</small>`).

---

## 4. Multi-Image Presentation System (Content Designer Guide)

The blog supports four distinct presentation modes for adjacent images, designed with a minimal, non-invasive Two-Tier authoring model. Fenced containers (`::: name`) and alert-style blockquotes (`> [!NAME]`) coexist to produce identical output.

### The Four Presentation Modes

#### 1. Ungrouped / Stacked (Default Independent Flow)
- **Authoring**: Separate images with an empty **blank line**.
- **Result**: Each image compiles to an independent `<p>` tag, rendering full-width and centered with standard margins.
- **When to use**: Independent full-page diagrams, terminal captures requiring full width, or sequential walkthrough steps separated by instructional text.
```markdown
![Architecture Overview](arch.webp)

![Database Schema](db.webp)
```

#### 2. Auto-Fit Responsive Grid (`image-grid` / `::: grid` / `> [!GRID]`)
- **Authoring**: Place consecutive images in the **same paragraph** (without blank lines) or wrap in `::: grid` / `> [!GRID]`.
- **Result**: CSS Grid with auto-fitting responsive columns (`minmax(260px, 1fr)`), 16:10 aspect ratio, and hover zoom.
- **When to use**: 2 to 4 technical screenshots, side-by-side configuration dialog comparisons, benchmark results, or 3 to 6 conference presentation photos.
```markdown
<!-- Zero-syntax automatic grid (same paragraph) -->
![Config Dialog A](dialog-a.webp) ![Config Dialog B](dialog-b.webp)

<!-- Or explicit container -->
::: grid
![Step 1](step1.webp)
![Step 2](step2.webp)
![Step 3](step3.webp)
:::
```

#### 3. Horizontal Scroll-Snap Strip (`::: strip` / `> [!STRIP]`)
- **Authoring**: Wrap image links in `::: strip` or `> [!STRIP]`.
- **Result**: Zero-JS horizontal filmstrip with touch scroll-snap, 2:3 card aspect ratio, and hover elevation. Outbound links (such as Amazon affiliate links) remain fully clickable.
- **When to use**: Book recensions and reading lists (5 to 10 covers), horizontal wizard progressions, or compact gadget collections.
```markdown
::: strip
[![Book 1](cover1.webp)](https://amazon.com/dp/...)
[![Book 2](cover2.webp)](https://amazon.com/dp/...)
[![Book 3](cover3.webp)](https://amazon.com/dp/...)
:::
```

#### 4. Expandable Event Album / Lightbox Gallery (`::: gallery` / `> [!GALLERY]`)
- **Authoring**: Wrap event photos in `::: gallery` or `> [!GALLERY]`.
- **Result**: 3-column mosaic plate with high-resolution lightbox modal inspection on click.
- **When to use**: Conference recaps, summit photo drops (DevFest, MSCC, Google Summits) with 6 to 9+ photos, eliminating infinite vertical scroll bloat.
```markdown
::: gallery
![Keynote Stage](stage.webp)
![Audience Gathering](crowd.webp)
![Workshop Team](team.webp)
![Speaker Panel](panel.webp)
![Community Swag](swag.webp)
:::
```

### Content Designer Decision Matrix

| Content Archetype | Image Count | Recommended Mode | Authoring Syntax |
| :--- | :---: | :--- | :--- |
| **Linear Step / Full Diagram** | 1 – 2 | **Ungrouped / Stacked** | Separate with blank lines |
| **Side-by-Side UI Comparison** | 2 – 4 | **Auto-Fit Grid** | Back-to-back in same paragraph (or `::: grid`) |
| **Book Recension / Shelf** | 4 – 10 | **Scroll-Snap Strip** | `::: strip` or `> [!STRIP]` |
| **Conference / Event Album** | 6 – 9+ | **Expandable Gallery** | `::: gallery` or `> [!GALLERY]` |

---

## 5. Frontmatter, Metadata & Open Graph Conventions (DRY Principle)

Apply the **DRY (Don't Repeat Yourself)** principle to DocFX frontmatter:
- Populate the primary **`image`** attribute with the main WebP hero asset path:
  ```yaml
  image: content/images/YYYY/MM/<uid>.webp
  ```
- **Automated Open Graph (`1200 × 630 px`) Card Generation**:
  - Running `python3 scripts/localize-assets.py` automatically generates an intelligent Open Graph preview card saved alongside the hero image as `<uid>-og.webp` (e.g. `content/images/YYYY/MM/<uid>-og.webp`).
  - **Composition**: Scaled hero backdrop with gentle depth blur, left-attached 42% translucent frosted-glass plates hugging the balanced multi-line title and bottom-left author attribution (`Jochen Kirstätter` • `jochen.kirstaetter.name`), and a bottom-right frosted-glass card housing a scannable QR code of the extension-less article URL (`https://jochen.kirstaetter.name/<uid>`).
  - The script automatically wires `ogImage: content/images/YYYY/MM/<uid>-og.webp` into frontmatter.
- **Manual Open Graph Image Overrides**:
  - At any time, a designated custom Open Graph image can be produced manually by the author to overwrite the default generated one.
  - Simply place your custom 1200×630 image at `content/images/YYYY/MM/<uid>-og.webp` (or set `ogImage: content/images/YYYY/MM/<custom-name>.webp` in the frontmatter).
  - The automated script checks for existing files and will never overwrite user-crafted custom Open Graph images.
- Leave redundant legacy image fallback attributes empty (`imageUrl: ''`, `twitterImageUrl: ''`, `featureImage: ''`) unless a specific third-party integration explicitly requires a full URL override.
- Ensure `uid`, `title`, `date`, `status`, `type`, `description`, `tags`, and `keywords` are properly populated.

---

## 6. Draft Assets & Research Workspace Isolation

To keep published content and public build artifacts pristine:
- Store all research notes, downloaded source materials, prompt logs, and working screenshots in an isolated per-draft directory:
  ```
  posts/draft/assets/<uid>/
  ```
- Maintain a dedicated **`resources.md`** file inside this folder tracking:
  - Official documentation URLs and blog announcements.
  - Social media citations (exact post URLs and timestamps).
  - Media generation prompts, models used (e.g. *Gemini 3.1 Flash Image*), and generated resolution buckets.
  - Raw testing notes, friction points, and community Q&A transcripts.

---

## 7. Publication Lifecycle

1. **Drafting**:
   - File created at `posts/draft/<uid>.md`.
   - Flags set: `status: draft`, `isDraft: true`.
2. **Review & Emulation**:
   - Generate draft index and build: `npm run build:draft`.
   - Preview locally: `firebase emulators:start`.
3. **Promotion to Production (Fast-Track CLI)**:
   - Run the automated fast-track promotion and verification pipeline:
     ```bash
     # Fast-track promotion, asset verification, and build:
     npm run publish:post -- --slug <uid> [--commit]
     ```
   - *Direct manual equivalent*:
     - Move markdown file from `posts/draft/<uid>.md` to `posts/published/<uid>.md`.
     - Update frontmatter: `status: published`, `isDraft: false`, `publishedAt: YYYY-MM-DDTHH:MM:SSZ`, `updatedAt: YYYY-MM-DDTHH:MM:SSZ`.
     - Run production build and pre-deploy check: `npm run build`.
4. **Post-Publication Outreach Audit & Calibration**:
   - Immediately following promotion, review companion social media drafts archived in `posts/draft/assets/<uid>/resources.md`.
   - Calibrate the outreach text to match the **actual final published content**, incorporating any late editorial revisions, refined arguments, and the final permalink.
   - Enforce strict platform character budgets (X: 280 chars with `t.co` URL; BlueSky: 300 chars hard limit; Mastodon: 500 chars; LinkedIn: 800–1,500 chars) with verified character tallies before presenting copy.
5. **Production Deployment**:
   - Obtain **explicit user approval** before executing deployment.
   - Run: `npm run deploy` (requires clean Git status passing `scripts/check-clean-posts.py`).
