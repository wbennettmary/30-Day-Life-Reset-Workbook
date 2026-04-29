# Phase 4 QA Checklist — Final Sign-Off

**Phase:** 4 — Canva Design
**When to run this:** AFTER all 56 pages built, both PDFs exported, all 5 mockups created.
**If any check fails:** fix first, re-export if needed, then re-run the failed section. Do NOT advance to Phase 5 until every check is green.

---

## A. Daily Page Sanity (run on 5 random daily pages)

Pick 5 days at random — suggested: Day 3, Day 10, Day 17, Day 24, Day 30 (these match the motivation-touchpoint days in the manuscript).

For each:

- [ ] All 11 schema fields visible: Day_Number, Title, Goal, Task_1, Task_2, Task_3, Quick_Win, Why_It_Works, Reflection, Mood_Scale, Tomorrow_Focus
- [ ] No truncation (`...` or visibly cut-off text)
- [ ] No placeholder text leaked (`{Title}`, `{Goal}`, etc.)
- [ ] Mood emoji renders as `😊 / 😐 / 😔` — not boxes, not `?`
- [ ] Page background is `#FAF8F6` (cream), NOT white
- [ ] Title hierarchy reads: small DAY label → large title → goal sentence
- [ ] Sage accent rule visible under title

---

## B. Acceptance Tests From Master File

These come straight from `master_life_reset_v4.json` → `qa_and_iteration.acceptance_tests`. Run each:

- [ ] **Quick Start usability** — open the PDF, jump to page 02 (Quick Start), and time how long it takes to understand "do one thing, then come back tomorrow." Must be under 60 seconds.
- [ ] **One primary action per daily page** — no daily page should feel like it has 6+ competing focal points. Tasks 1/2/3 + Quick Win is the design. If it reads cluttered, the layout failed.
- [ ] **No visually overwhelming pages** — flip through in Canva preview. Every page should breathe.
- [ ] **Checkpoints give explicit restart permission** — pages 15, 24, 33 must contain a "you can pick up here" or "missed days are fine" line. Page 44 (Day 30) is the closing — it's allowed to skip the restart language.
- [ ] **Zero banned words** — search the design for: `transform`, `journey`, `unlock`, `level up`, `optimize`, `hack`, `dominate`, `crush`, `supercharge`. Use Canva's text search or copy each page's text into a doc and Ctrl+F.
- [ ] **CSV fields under 200 chars** — already verified in pre-flight. Confirm by spot-checking 3 daily pages that the longest field doesn't visibly overflow its box.
- [ ] **Both PDFs open cleanly** — Adobe Reader and iPhone Files (or Apple Preview).
- [ ] **Mockups look premium** — could pass for a commercial wellness product on Amazon.

---

## C. Tone & Voice Spot Check

Pull 3 random pages and read the body text aloud. Ask:

- [ ] Does it sound like "a calm friend who has been where you are"?
- [ ] Does it use any of the must-use phrases somewhere in the workbook? (`Let's`, `You've got this`, `Small wins add up`, `Progress, not perfection`)
- [ ] Does it avoid all must-avoid phrases? (`Transform your life overnight`, `Just commit harder`, `Ultimate solution`, hustle verbs)
- [ ] Does the gentle missed-day language appear at Days 8, 15, 22?
- [ ] Are motivation touchpoints present at Days 1, 3, 10, 17, 24, 30?

---

## D. Behavioral Pacing Audit (already done in Phase 2.5, re-verify visually)

- [ ] Days 1–10 read as emotional/awareness work — no big goal-setting tasks
- [ ] Days 11–20 introduce structured habits at most one new category per week
- [ ] Days 21–30 shift to identity-level reflection and future planning
- [ ] No week introduces more than 3 new behaviors

---

## E. Visual System Consistency

- [ ] Every page uses background `#FAF8F6` (or the warm card variant on prompt pages)
- [ ] Sage `#848B6F` appears on every page in some form (rule, leaf, or accent)
- [ ] Headers all use Montserrat
- [ ] Body all uses Inter (or Helvetica Neue fallback)
- [ ] No third font snuck in
- [ ] Rounded corners on all cards (12 or 16 px)
- [ ] Botanical sprig appears on at least: cover, week dividers, checkpoints, bonus pages

---

## F. File Delivery Verification

```
30-day-life-reset/exports/
  ├── Main_Workbook_US_Letter.pdf       [size: 8–25 MB expected]
  ├── Main_Workbook_A4.pdf              [size: 8–25 MB expected]
  ├── Quick_Start_Guide.pdf             [size: <2 MB expected]
  └── mockups/
      ├── 01_cover_flatlay.jpg          [2000×2000, <1 MB]
      ├── 02_interior_spread.jpg        [2000×2000, <1 MB]
      ├── 03_habit_tracker_closeup.jpg  [2000×2000, <1 MB]
      ├── 04_phone_screen.jpg           [2000×2000, <1 MB]
      └── 05_lifestyle_bundle.jpg       [2000×2000, <1 MB]
```

- [ ] All 8 files exist at the paths above
- [ ] File sizes within expected ranges
- [ ] All filenames match exactly (lowercase, underscores, no spaces)

---

## G. Two Cover Caveats (carry-over from upload verification)

You were told about these during the kickoff for this phase. Confirm one of the two paths was taken:

**Front cover:**
- [ ] File renamed from `front_cover.png.png` to `front_cover.png` before import
- [ ] Imported to Canva successfully
- [ ] Acknowledged the soft DPI (1103×1426 ≈ 133 DPI on US Letter — fine for digital)

**Back cover:**
- [ ] Aspect ratio handled — either cropped to fit US Letter or letterboxed on `#FAF8F6`
- [ ] No content lost off-frame (tagline, what's-inside box, price block all visible)

---

## H. Sign-off

When every box above is checked, you are clear for HANDOFF return.

Reply to Claude:

```
Canva done, page count: 56
```

That triggers Phase 5 (Packaging) — Claude will assemble the ZIP and write CHANGELOG.md.

---

## If anything failed

Use the issue routing from the master file:

| Issue type | Where to fix |
|---|---|
| Daily page truncation or layout broken | `01_master_template_spec.md` — fix master, re-run Bulk Create |
| Wrong content in a slot | `02_bulk_create_guide.md` — re-map columns |
| Non-daily page tone/clarity issue | `03_non_daily_pages_brief.md` — re-design that page |
| Page order wrong | `04_assembly_checklist.md` — reorder pages |
| Mockup looks generic | `05_mockup_brief.md` — review composition rules |
| Banned word slipped through | Re-open the source chunk, fix, re-bulk-create that day |
| Behavioral pacing issue | Back to Phase 2.5 — flag the day for Gemini re-audit |
