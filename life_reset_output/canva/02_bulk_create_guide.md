# Bulk Create Guide — CSV → 30 Daily Pages

**Phase:** 4 — Canva Design
**Input:** `30-day-life-reset/csv/daily_pages.csv` (verified clean — 31 rows, 11 fields, max 115 chars)
**Output:** 30 daily pages generated from the master template
**Time estimate:** 15 minutes if test passes first try, ~45 minutes if you have to iterate.

---

## Step 0 — Pre-flight (do not skip)

Open the CSV in a **plain text editor** (VS Code, Sublime, Notepad on Windows — NOT Excel; Excel mangles emojis and adds BOMs).

Verify by eye:
- Row 1 = headers, exactly: `Day_Number,Title,Goal,Task_1,Task_2,Task_3,Quick_Win,Why_It_Works,Reflection,Mood_Scale,Tomorrow_Focus`
- Row 2 starts with `1,Day 1: Check In With Yourself,...`
- Last data row starts with `30,Day 30: You Did It,...`
- Every row contains `😊 / 😐 / 😔` (this is the Mood_Scale column — Canva ignores it because the master template has the emoji as fixed text, but the column must exist for the schema to validate)

If any header is renamed, renamed back, or wrapped in quotes, **fix the source file before uploading**. Renaming after Canva mapping breaks Bulk Create.

---

## Step 1 — Open Canva Bulk Create

1. Open the master design: **`30DLR — Master Daily Template`**.
2. Left sidebar → **Apps** → search "Bulk Create" → open it.
3. Click **Upload CSV**.
4. Select `daily_pages.csv` from `30-day-life-reset/csv/`.

Canva parses and shows a preview table with 30 rows.

> If Canva shows fewer than 30 rows, the CSV has a parse problem (likely an unescaped comma or quote). Open in plain text editor, find the broken row, fix, re-upload.

---

## Step 2 — Map columns to placeholders

Canva will list every named placeholder it found in the master design and ask which CSV column to bind to each.

| Canva placeholder | Bind to CSV column |
|---|---|
| `Day_Number` | `Day_Number` |
| `Title` | `Title` |
| `Goal` | `Goal` |
| `Task_1` | `Task_1` |
| `Task_2` | `Task_2` |
| `Task_3` | `Task_3` |
| `Quick_Win` | `Quick_Win` |
| `Why_It_Works` | `Why_It_Works` |
| `Reflection` | `Reflection` |
| `Tomorrow_Focus` | `Tomorrow_Focus` |

> The `Mood_Scale` column should be visible in Canva's column list but **DO NOT bind it to anything**. It exists in the CSV only to keep the schema locked.

---

## Step 3 — TEST WITH ONE ROW FIRST (this is the rule)

Most failures happen here. Find them now, not after generating 30 pages.

1. In Bulk Create's row picker, **select only Day 1** (first row).
2. Click **Generate** (or "Continue" then "Connect data").
3. Wait. Canva creates one new page in the design.

### Test page QA — check every box

- [ ] Day number reads `1`, not `Day_Number` or `{Day_Number}` (placeholder text leaked)
- [ ] Title reads "Day 1: Check In With Yourself" — no truncation, no `...`
- [ ] Goal reads in full, no overflow into the middle zone
- [ ] All 3 tasks rendered, no truncation
- [ ] Quick Win line rendered
- [ ] Why It Works line rendered
- [ ] Reflection rendered
- [ ] `😊 / 😐 / 😔` is the literal mood row (and it's only there ONCE — the fixed text element from the master)
- [ ] Tomorrow Focus rendered
- [ ] No box shows the wrong content (e.g. Reflection appearing in the Why It Works slot — would mean a mapping mistake)
- [ ] Page background is `#FAF8F6`, not white
- [ ] No banned words visible (transform, journey, unlock, level up, optimize, hack, dominate, crush, supercharge)

If ANY box fails:
- **Truncation** → enlarge the text box on the master template, or set the text element to "auto-resize" → re-test.
- **Wrong content in a slot** → re-open Bulk Create → re-map columns.
- **Placeholder name visible** → the master template binding broke. Right-click the text → Connect data → re-bind.
- **Mood row missing** → the literal text was deleted or the binding accidentally consumed it. Re-add as plain text on the master.

Re-run the test with Day 1 only until everything passes.

---

## Step 4 — Generate the remaining 29

1. Re-open Bulk Create.
2. Select rows 2–30 (Days 2 through 30).
3. Click **Generate**.
4. Wait — this can take 1–3 minutes for 29 pages.

When complete, you'll have 30 daily pages added to the design.

### Post-generation spot check (3 random days)

Pick **Day 8**, **Day 17**, and **Day 30** and inspect each:
- Day 8 has the missed-day reset language somewhere (check the chunk if you forget what it says)
- Day 17 motivation touchpoint is present
- Day 30 reads cleanly — closing energy

If any spot-check fails, look at the source row in the CSV (it shouldn't fail — the Gemini audit caught these — but verify before moving on).

---

## Step 5 — Delete the master "preview" page

The original master template page (with the dummy Day 1 content from build) is still in your design. It will end up as page 1 of your PDF if you don't remove it.

1. Find the page with dummy content.
2. Right-click → Delete page.

Now the design contains only the 30 generated daily pages, in order.

---

## Step 6 — Reorder if needed

Canva sometimes generates Bulk Create pages in CSV order (good) but occasionally inserts them in reverse or after the master. Confirm Days run 1 → 30 from page 1 to page 30.

If out of order, drag pages in the page-grid view until correct.

---

## Common Failure Modes & Fixes

| Symptom | Cause | Fix |
|---|---|---|
| Mood emoji shows as `?` or boxes | Excel saved CSV with wrong encoding | Re-open original CSV in VS Code, save as UTF-8 (no BOM), re-upload |
| One day missing | Empty row in CSV | Open CSV, check for stray blank line, save, re-upload |
| Placeholder text still showing | Binding wasn't completed | Re-do Step 2 — Canva needs every placeholder mapped explicitly |
| Title overflows into Tasks zone | Master template text box too small | Enlarge the title box on master, enable auto-resize, re-run test row |
| Bulk Create button greyed out | Pro/Teams feature only | Confirm you are signed into a Canva Pro or Teams account |
| Different fonts on different pages | Brand Kit not applied or font missing | Re-set fonts on master template, regenerate |

---

## Done criteria

- 30 daily pages exist in the design
- Test row passed all 11 checks in Step 3
- Spot-check on Days 8, 17, 30 passed
- Master preview page deleted
- Pages ordered Day 1 → Day 30

When all five are true, move to `03_non_daily_pages_brief.md`.
