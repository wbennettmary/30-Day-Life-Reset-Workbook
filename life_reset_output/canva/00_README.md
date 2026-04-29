# Phase 4 — Canva Build Sheets (Index)

**Generated:** 2026-04-27
**Mode:** Fully manual Canva build (no Canva MCP)
**Use these in order. Do not skip ahead.**

| # | File | Purpose | Read time |
|---|---|---|---|
| 01 | `01_master_template_spec.md` | Build the master daily-page template in Canva. Color palette, fonts, layout grid, named placeholders. | 8 min |
| 02 | `02_bulk_create_guide.md` | Run Canva Bulk Create on `daily_pages.csv`. Test with one row, then generate 30. | 6 min |
| 03 | `03_non_daily_pages_brief.md` | Design the 26 manual pages: covers, front matter, week dividers, checkpoints, trackers, bonuses. | 12 min |
| 04 | `04_assembly_checklist.md` | Final 56-page order. Export US Letter PDF, A4 PDF, Quick Start PDF. | 6 min |
| 05 | `05_mockup_brief.md` | Create 5 Etsy listing images (cover flat lay, interior spread, habit close-up, phone, bundle). | 8 min |
| 06 | `06_qa_checklist.md` | Final sign-off before HANDOFF-3 return. | 5 min |
| 07 | `07_ai_starter_design.md` | AI-generated reference page (Canva MCP). Optional starting point. | 2 min |

**Total reading:** ~45 min. **Total Canva execution:** ~6–10 hours depending on your speed and how many test iterations.

---

## Two cover caveats to handle before you start

1. **Rename `front_cover.png.png` → `front_cover.png`** (currently has a double extension at the project root).
2. **Back cover is 2:3 ratio, not US Letter.** You'll need to crop or letterbox in Canva. See `03_non_daily_pages_brief.md` §A for the two options.

---

## Source files used by Phase 4

| What | Path |
|---|---|
| Master orchestration | `master_life_reset_v4.json` |
| Final chunks (post-Gemini audit) | `30-day-life-reset/content/raw/chunk_01.md` through `chunk_09.md` |
| Daily pages CSV | `30-day-life-reset/csv/daily_pages.csv` |
| Front cover image | `front_cover.png.png` (rename to `front_cover.png` before import) |
| Back cover image | `back_cover.png` |
| Pre-existing Canva guide | `30-day-life-reset/canva/CANVA_MCP.md` (reference only — Phase 4 uses these new build sheets) |

---

## Output files Phase 4 must produce

| What | Where |
|---|---|
| Main workbook PDF (US Letter) | `30-day-life-reset/exports/Main_Workbook_US_Letter.pdf` |
| Main workbook PDF (A4) | `30-day-life-reset/exports/Main_Workbook_A4.pdf` |
| Quick Start lead magnet PDF | `30-day-life-reset/exports/Quick_Start_Guide.pdf` |
| 5 Etsy mockup JPGs | `30-day-life-reset/exports/mockups/` |

---

## When everything is done

Reply to Claude with:
```
Canva done, page count: 56
```

That advances the project to Phase 5 (Packaging).
