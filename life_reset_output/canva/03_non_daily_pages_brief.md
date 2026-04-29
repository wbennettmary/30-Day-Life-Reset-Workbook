# Non-Daily Pages Design Brief — 26 Pages

**Phase:** 4 — Canva Design
**Source content:** `30-day-life-reset/content/raw/chunk_01.md` through `chunk_09.md`
**Page total to build manually:** 26 (everything except the 30 Bulk Create daily pages)

Use the same color/font system as the master template. **Borrow the bottom warm card (`#EFE8DF`) sparingly — only on pages that ask the reader to write something — so daily pages stay visually distinct from setup/checkpoint pages.**

---

## A. Covers (2 pages)

### Page 01 — Front Cover
- **Source:** `front_cover.png.png` at project root
- **Action:** Rename the file to `front_cover.png` (drop the second `.png`) before importing.
- **Import:** Canva → Uploads → drag the renamed PNG → drag onto blank US Letter page → set as background, fill page (no margin).
- **Resolution caveat:** Source is 1103×1426. On US Letter (8.5×11), that's ~133 DPI — soft for print. Acceptable for digital PDF. If you plan a print-on-demand listing later, regenerate the cover at 2550×3300.

### Page 56 — Back Cover
- **Source:** `back_cover.png` at project root
- **Aspect ratio caveat:** Source is 1024×1536 (2:3 ratio), NOT US Letter (≈ 0.773). Importing as-is leaves white bands or crops content.
- **Two options:**
  1. (Recommended) **Crop to fit US Letter** — scale to fill 8.5×11, content will lose some top/bottom area. Check that the tagline, what's-inside box, and price block all stay inside the safe area.
  2. **Center on cream background** — place the image at native ratio with `#FAF8F6` letterboxing top and bottom. Less elegant but preserves all content.
- Pick option 1 if the corner sprig and barcode block survive the crop.

---

## B. Front Matter (4 pages — pages 02, 03, 04, 05)

### Page 02 — Quick Start
- **Goal:** Reader can begin within 60 seconds of opening this page.
- **Source:** `chunk_01.md` → "Quick Start page" section.
- **Layout:**
  - Top sage rule, "QUICK START" in upper-case Montserrat Light 14 pt + tracking.
  - Title: **You don't need to read everything.** (Montserrat SemiBold 32 pt, centered)
  - Three numbered steps (1, 2, 3) — large numerals in sage `#848B6F`, body in Inter 12 pt:
    1. Open to Day 1.
    2. Do one task. Any task.
    3. Come back tomorrow.
  - Below that, a single-line invitation: "That's it. You've already started."
  - Generous bottom whitespace. No card. No icons except an optional sage sprig in one corner.

### Page 03 — Why You Feel Stuck
- **Source:** `chunk_01.md` → "Why You Feel Stuck" section (3 paragraphs).
- **Layout:**
  - Heading: "Why You Feel Stuck" (Montserrat SemiBold 28 pt, left-aligned)
  - Three paragraphs, body 12 pt, line height 1.5, max line width 5.5 in.
  - End with the hopeful closing line set apart in italic accent serif: "*This isn't a flaw. It's a signal.*" (or whatever the chunk's ending line is — pull verbatim).
  - Pull-quote treatment: thin sage rule above and below the closing line.

### Page 04 — How to Use This Workbook
- **Source:** `chunk_01.md` → "How to Use" section.
- **Layout:**
  - Heading: "How to Use This Workbook"
  - 4–5 short rules, each on its own line, preceded by a sage leaf bullet:
    - You can skip days.
    - You can repeat days.
    - You can pause.
    - There is no failure mode here.
  - Below: a soft callout in the warm card style (`#EFE8DF`, 16 px radius): "Missed a day? That's the reset too. Pick up here." (verbatim from chunk if present)
  - Footer: "Read this once. Then close it and start."

### Page 05 — Life Audit
- **Source:** `chunk_02.md` → "Life Audit" section (8 life areas).
- **Layout:**
  - Heading: "Life Audit"
  - Subtitle (italic accent serif): "Where you are right now — without judgment."
  - 8 rows in a 2-column grid (4 areas per column):
    - Health · Energy · Relationships · Work
    - Finances · Home · Growth · Joy
  - Each row: area name on the left, then **a 1–10 scale of small dots** the reader circles, then a short line for "Now → Want."
  - Use sage dots, with the empty/filled state visible (open circle = unselected).
  - Bottom: "Use these scores to pick where Day 1 starts." (or pull from chunk).

---

## C. Vision + Focus (1 page — page 06)

### Page 06 — 90-Day Vision + 30-Day Focus
- **Source:** `chunk_02.md` → "90-Day Vision page" + "30-Day Focus page" combined.
- **Layout:**
  - Two stacked sections divided by a sage rule.
  - **Top half — 90-DAY VISION**
    - Three prompts, each on its own line, with a generous line break for handwriting:
      - "In 90 days, I want to feel..."
      - "The biggest shift I want to make is..."
      - "The one thing holding me back is..."
  - **Bottom half — 30-DAY FOCUS**
    - One large box (warm card, `#EFE8DF`, 16 px radius): "My one intention for these 30 days is:" with 4 lines of writing space underneath.
- Keep both halves visually quiet. This is where the reader commits.

---

## D. Week Overviews (4 pages — pages 07, 16, 25, 34)

Same layout for all four. Pull copy from the chunk's "Week N Overview" section.

| Page | Week | Theme | Source |
|---|---|---|---|
| 07 | Week 1 | Foundation — Energy & Awareness | `chunk_03.md` overview |
| 16 | Week 2 | Momentum — Habits & Productivity | `chunk_04.md` overview |
| 25 | Week 3 | Growth — Body, Mind, Environment | `chunk_05.md` overview |
| 34 | Week 4 | Integration — Identity, Values, Future | `chunk_06.md` overview |

**Layout:**
- Top: small label "WEEK [N]" in sage uppercase Montserrat Light 12 pt + tracking
- Title: theme name (Montserrat SemiBold 32 pt, centered)
- Below: 2–3 short paragraphs from chunk overview (Inter 12 pt, line height 1.5)
- Bottom warm card (`#EFE8DF`, 16 px radius): the missed-day-reset note (Weeks 2, 3, 4 only — Week 1 doesn't need one)
- Decorative single sage leaf sprig top-right
- Generous whitespace — this is a breath page

---

## E. Checkpoint Pages (4 pages — pages 15, 24, 33, 44)

Same layout for all four. Pull copy from `chunk_07.md`.

| Page | Day | Source |
|---|---|---|
| 15 | Day 7 | `chunk_07.md` → Day 7 Checkpoint |
| 24 | Day 14 | `chunk_07.md` → Day 14 Checkpoint |
| 33 | Day 21 | `chunk_07.md` → Day 21 Checkpoint |
| 44 | Day 30 | `chunk_07.md` → Day 30 Checkpoint |

**Layout:**
- Top: "DAY [N] CHECKPOINT" in sage uppercase
- Title (large): "You made it to Day [N]. That matters." (Montserrat SemiBold 28 pt)
- Five reflection prompts, each with 2 lines of writing space:
  - What worked this week
  - What felt heavy
  - One thing I'm proud of
  - One thing to adjust
  - Restart permission note (verbatim from chunk — never shame)
- Day 30 page: **swap "Restart permission" for a closing line** like "You finished. Now what?" + small bridge to bonus 90-day roadmap.

---

## F. Trackers (8 pages — pages 45–52)

### Page 45 — Monthly Habit Tracker Grid
- **Source:** `chunk_08.md` → Monthly Habit Grid section.
- **Layout:** 6 habits × 30 days grid. First column is habit name (sleep, water, move, read, journal, one personal). Top row is days 1–30. Cells are small open circles the reader fills in.
- Heading: "Habit Tracker"
- Footer note: "One filled circle is enough today."

### Page 46 — Mood Tracker
- **Source:** `chunk_08.md` → Mood Tracker section.
- **Layout:** 30 cells (6×5 grid). Above each cell, the day number. Inside the cell, three tiny emoji options to circle: 😊 / 😐 / 😔.
- Heading: "Mood Tracker"
- Footer: "There are no wrong moods."

### Page 47 — Weekly Review Template
- **Source:** `chunk_08.md` → Weekly Review Template.
- **Layout:** Reusable single page with 4–5 prompts and writing space.
- Add small instruction at top: "Photocopy or duplicate this page each week."

### Pages 48–52 — Category Trackers (5 pages)
- **Source:** `chunk_08.md` → 5 Category Trackers (health, productivity, home, money, relationships).
- **One page per category.** Each has:
  - Heading: category name
  - 6–8 simple checkbox rows
  - A "Notes" area at the bottom (4–5 lines)
- Use the warm card style for the Notes area only. Keep checkboxes on the main page background.

---

## G. Bonuses (3 pages — pages 53, 54, 55)

### Page 53 — 50 Tiny Habits
- **Source:** `chunk_09.md` → "50 Tiny Habits" section (sorted by category).
- **Layout:** 6 categories (health, mind, productivity, home, money, relationships), 6–9 habits per category, displayed in 2 columns.
- Each habit prefixed with a small sage open circle (so the reader can mark it).
- Heading: "50 Tiny Habits"
- Subtitle (italic): "All under 5 minutes. Pick one. Try it twice."

### Page 54 — 7-Day Emergency Reset
- **Source:** `chunk_09.md` → "7-Day Emergency Reset" section.
- **Layout:** A condensed weekly grid — 7 cells (M–Su), each with one ultra-simple action.
- Heading: "7-Day Emergency Reset"
- Subtitle: "When you need to start fast."
- Footer card: "Use this when life gets messy. Then come back to Day 1."

### Page 55 — 90-Day Continuation Roadmap
- **Source:** `chunk_09.md` → "90-Day Continuation Roadmap" section.
- **Layout:** 3 columns (one per month), each with a theme and 3 focus areas.
- Heading: "What Comes After Day 30"
- Footer line: "Slow is sustainable. You've got this."

---

## H. Universal QA per page

For each non-daily page you finish, run:

- [ ] No banned words (transform, journey, unlock, level up, optimize, hack, dominate, crush, supercharge)
- [ ] Includes a "must-use" phrase where appropriate (`Let's`, `You've got this`, `Small wins add up`, `Progress, not perfection`)
- [ ] Whitespace generous — no page feels visually loud
- [ ] No more than 2-line paragraphs in body copy
- [ ] Sage leaf or sprig present on at least one of: cover, week dividers, checkpoint pages, bonus pages
- [ ] Title hierarchy reads cleanly (small label → big title → body)
- [ ] No emoji other than `😊 / 😐 / 😔` on Mood Tracker (page 46) and within daily pages

When all 26 non-daily pages pass, move to `04_assembly_checklist.md`.
