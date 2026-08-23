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
5. **Technical Quirks & Missing Functionality**: Dedicate a section to friction points, platform-specific differences (e.g. Linux desktop vs macOS, CLI vs GUI), or feature gaps when reviewing new tools.
6. **Key Takeaways & References**: Provide a concise summary and link directly to official documentation, tools, or repos.
7. **Join the Conversation (CTA)**: Conclude with a warm, signature prompt inviting readers to connect and discuss on social platforms (X: `@JKirstaetter`, BlueSky: `@jochen.kirstaetter.name`, Mastodon: `@JKirstaetter`, RSS feed).
8. **Picture Credits & Attribution**: Include a footer credit line for AI-generated visuals or photography (e.g. `<small>Picture credits: ...</small>`).

---

## 4. Frontmatter, Metadata & Open Graph Conventions (DRY Principle)

Apply the **DRY (Don't Repeat Yourself)** principle to DocFX frontmatter:
- Populate the primary **`image`** attribute with the main WebP hero asset path:
  ```yaml
  image: content/images/YYYY/MM/<slug>.webp
  ```
- **Automated Open Graph (`1200 × 630 px`) Card Generation**:
  - Running `python3 scripts/localize-assets.py` automatically generates an intelligent Open Graph preview card saved alongside the hero image as `<slug>-og.webp` (e.g. `content/images/YYYY/MM/<slug>-og.webp`).
  - **Composition**: Scaled hero backdrop with gentle depth blur, left-attached 42% translucent frosted-glass plates hugging the balanced multi-line title and bottom-left author attribution (`Jochen Kirstätter` • `jochen.kirstaetter.name`), and a bottom-right frosted-glass card housing a scannable QR code of the extension-less article URL (`https://jochen.kirstaetter.name/<slug>`).
  - The script automatically wires `ogImage: content/images/YYYY/MM/<slug>-og.webp` into frontmatter.
- **Manual Open Graph Image Overrides**:
  - At any time, a designated custom Open Graph image can be produced manually by the author to overwrite the default generated one.
  - Simply place your custom 1200×630 image at `content/images/YYYY/MM/<slug>-og.webp` (or set `ogImage: content/images/YYYY/MM/<custom-name>.webp` in the frontmatter).
  - The automated script checks for existing files and will never overwrite user-crafted custom Open Graph images.
- Leave redundant legacy image fallback attributes empty (`imageUrl: ''`, `twitterImageUrl: ''`, `featureImage: ''`) unless a specific third-party integration explicitly requires a full URL override.
- Ensure `uid`, `title`, `slug`, `date`, `status`, `type`, `description`, `tags`, and `keywords` are properly populated.

---

## 5. Draft Assets & Research Workspace Isolation

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

## 6. Publication Lifecycle

1. **Drafting**:
   - File created at `posts/draft/<slug>.md`.
   - Flags set: `status: draft`, `isDraft: true`.
2. **Review & Emulation**:
   - Generate draft index and build: `npm run build:draft`.
   - Preview locally: `firebase emulators:start`.
3. **Promotion to Production**:
   - Move markdown file from `posts/draft/<slug>.md` to `posts/published/<slug>.md`.
   - Update frontmatter:
     ```yaml
     status: published
     isDraft: false
     publishedAt: YYYY-MM-DDTHH:MM:SSZ
     updatedAt: YYYY-MM-DDTHH:MM:SSZ
     ```
   - Run production build and pre-deploy check: `npm run build`.
   - **Deployment**: Obtain **explicit user approval** before executing `npm run deploy` or deploying to Firebase.
