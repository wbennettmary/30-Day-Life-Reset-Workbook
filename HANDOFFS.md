# Manual Handoffs — Human + Other AI Actions Required

## HANDOFF-1 — ChatGPT Images 2.0 — Cover Generation
**Status:** ⏳ PENDING
**When:** Before Phase 2 starts
**Where:** ChatGPT → Images 2.0 tab (NOT GPT-4o image gen — use the dedicated Images 2.0 feature)
**Output dimensions:** 2550 x 3300 px (US Letter, 300 DPI)

### FRONT COVER PROMPT
See `covers/COVERS_README.md` for the full upgraded v2 prompt.
Save output as: `covers/front_cover.png`

### BACK COVER PROMPT
See `covers/COVERS_README.md` for the full upgraded v2 back cover prompt.
Save output as: `covers/back_cover.png`

**Return trigger:** `Covers done, starting Phase 2`

---

## HANDOFF-2 — Gemini 3.1 Pro (HIGH Thinking) — Full Behavioral Audit
**Status:** ⏳ PENDING
**When:** After ALL 9 chunks are generated and saved in content/raw/
**Where:** aistudio.google.com → select gemini-3.1-pro-preview → set thinking budget to HIGH
**Model:** `gemini-3.1-pro-preview`
**Thinking budget:** HIGH (maximum)

### HOW TO SET THINKING BUDGET TO HIGH IN AI STUDIO
1. Go to aistudio.google.com
2. New prompt → select model: gemini-3.1-pro-preview
3. Click gear icon / Advanced settings
4. Drag thinking budget slider to maximum
5. Confirm it shows HIGH or maximum before pasting content

### STEPS
1. In your terminal, run:
   `cat content/raw/chunk_0*.md > content/all_chunks_combined.md`
2. Open the combined file and confirm it has content from all 9 chunks
3. Open AI Studio with thinking budget set to HIGH
4. Paste the AUDIT PROMPT below
5. Then paste the full content of all_chunks_combined.md below the prompt
6. Submit — wait for the numbered fix list (may take 1-3 minutes with high thinking)
7. Return to Claude Code terminal:
   `PASTE RESULT:` followed by the full numbered list

### GEMINI 3.1 PRO AUDIT PROMPT (paste first, then paste manuscript)
```
You are a behavioral science reviewer and editorial auditor with a 1M token context window.
Read the entire 30-day life reset workbook manuscript below before outputting anything.

MANDATORY OUTPUT FORMAT:
Numbered list only. No prose. No summaries.
[Chunk/Day/Section] — [Severity: HIGH/MED/LOW] — [Issue type] — [Exact fix in one sentence]

Silence = approved. Output ONLY issues. If a section passes all checks, say nothing.

AUDIT CHECKLIST — check every item against every day:
1. Tasks exceeding 10 minutes realistically (HIGH)
2. Any week introducing more than 3 new behaviors total (HIGH)
3. Same task repeated across days with different wording (MED)
4. Missing motivation touchpoint at Days 3, 10, 17, 24 (MED)
5. Tone violations — perfectionism, guilt, shame, hustle culture language (HIGH)
6. Banned words present: transform, journey, unlock, level up, optimize, hack, dominate, crush, supercharge (MED)
7. Any field likely over 200 characters — count carefully (HIGH)
8. Emotional arc broken — should escalate: calm reassurance → gentle momentum → quiet confidence (MED)
9. Behavioral pacing violated — Days 1-10 must be emotional only, no big goal-setting (HIGH)
10. Any of the 11 daily schema fields missing from any day (HIGH)
    Required: Day_Number, Title, Goal, Task_1, Task_2, Task_3, Quick_Win, Why_It_Works, Reflection, Mood_Scale, Tomorrow_Focus
11. Missed-day reset language missing at Days 8, 15, 22 (MED)
12. Motivation touchpoint missing at Days 1, 3, 10, 17, 24, 30 (MED)

Rank output: ALL HIGH issues first, then MED, then LOW.
End with a line: TOTAL ISSUES: [N] (HIGH: [n] / MED: [n] / LOW: [n])

[PASTE all_chunks_combined.md CONTENT BELOW THIS LINE]
```
[Chunk 02/Before You Begin/Intro] — HIGH — Tasks exceeding 10 minutes realistically — Change the time estimate from "10–15 minutes" to "under 10 minutes" to adhere to the workbook's time limit.
[Chunk 03/Day 1/Task 3] — HIGH — Behavioral pacing violated — Replace the physical action of drinking water with an emotional reflection prompt.
[Chunk 03/Day 2/Task 3] — HIGH — Behavioral pacing violated — Replace the instruction to pick a physical morning behavior for tomorrow with a prompt to visualize tomorrow's mood.
[Chunk 03/Day 3/Task 2] — HIGH — Behavioral pacing violated — Replace the action of texting someone with an internal emotional reflection on a relationship they value.
[Chunk 03/Day 4/Task 1] — HIGH — Behavioral pacing violated — Change the physical space clearing task to a reflection on how visual clutter impacts their emotional state.
[Chunk 03/Day 5/Task 3] — HIGH — Behavioral pacing violated — Remove the action of slotting a task into an energy window and ask for a reflection on when they feel most drained.
[Chunk 03/Day 6/Task 3] — HIGH — Behavioral pacing violated — Replace the behavioral sleep hygiene adjustment with a reflection on how current sleep quality affects their emotional resilience.
[Chunk 04/Day 8/Task 3] — HIGH — Tone violations — Remove the phrase "Not an excuse" to eliminate guilt and shame framing.
[Chunk 04/Day 9/Task 1] — HIGH — Behavioral pacing violated — Change the behavioral action of checking phone screen time settings to a reflection on how their attention felt today.
[Chunk 05/Day 20/Tasks 1-3] — HIGH — Any week introducing more than 3 new behaviors total — Convert the avoided-task execution steps into a pure reflection on why the task is avoided to keep the week's total new behaviors at three.
[Chunk 05/Day 21/Task 2] — HIGH — Tone violations — Change "who you've actually been" to a neutral phrase like "how you have shown up" to avoid shaming the reader by implying they failed an ideal.
[Chunk 06/Day 30/Task 1] — HIGH — Tasks exceeding 10 minutes realistically — Reduce the 5-to-10 sentence letter requirement to a 1-to-2 sentence note to ensure completion under 10 minutes.
[Chunk 06/Day 30/Task 1] — HIGH — Any field likely over 200 characters — Change the 5-to-10 sentence letter requirement to 1-to-2 sentences to ensure the expected user input field stays under the 200 character limit.
[Chunk 03/Day 2/Task 1] — MED — Same task repeated across days with different wording — Adjust the prompt to focus on noticing their very first thought instead of repeating the stillness and body scan exercise from Day 1.
[Chunk 05/Day 20/Goal] — MED — Emotional arc broken — Soften the goal from confronting an avoided task to exploring resistance in order to maintain the arc of gentle momentum without sudden stress.
TOTAL ISSUES: 15 (HIGH: 13 / MED: 2 / LOW: 0)

**Return trigger:** `PASTE RESULT: [full numbered list from Gemini]`

---

## HANDOFF-2b — Gemini 3.1 Pro (LOW Thinking) — Fix Verification (Optional)
**Status:** ⏳ OPTIONAL — only if HIGH audit found 5+ HIGH severity issues
**When:** After Claude Code has applied all fixes from HANDOFF-2
**Where:** aistudio.google.com → gemini-3.1-pro-preview → thinking budget LOW
**Model:** `gemini-3.1-pro-preview`
**Thinking budget:** LOW (minimum)

### HOW TO SET THINKING BUDGET TO LOW
1. Same as above but drag thinking budget slider to minimum/low

### WHAT TO CHECK (targeted — not full manuscript)
Only paste the specific days that were flagged as HIGH severity.
Use this short prompt:
```
You are a behavioral reviewer doing a targeted spot-check.
Thinking budget is LOW — quick and efficient check only.

Review ONLY the days listed below. For each, confirm:
- All 11 schema fields present
- No field over 200 characters
- No banned words
- Task is realistically under 10 minutes

Output format: [Day N] — PASS or [Day N] — FAIL: [reason]

[PASTE ONLY THE SPECIFIC DAYS THAT WERE FLAGGED]
```

**Return trigger:** `Verification done: [X passes, Y fails]`

---

## HANDOFF-3 — Canva MCP — Design Production
**Status:** ⏳ PENDING
**When:** After csv/daily_pages.csv is verified clean
**Where:** Canva via MCP server in Antigravity terminal OR canva.com manually
**Reference:** See canva/CANVA_MCP.md for full Canva MCP integration guide

### CRITICAL FIRST STEP
Build and test the master template with ONE fake CSV row before generating all 30 pages.
Fail fast — do not batch generate before testing.

### STEPS
1. Create master daily page template in Canva (US Letter)
2. Apply color system: BG #FAF8F6, accent #848B6F, text #333333
3. Add text boxes named exactly: {Day_Number}, {Title}, {Goal}, {Task_1}, {Task_2}, {Task_3}, {Quick_Win}, {Why_It_Works}, {Reflection}, {Tomorrow_Focus}
4. Add fixed text element (NOT CSV-bound): 😊 / 😐 / 😔
5. Upload csv/daily_pages.csv via Bulk Create
6. Map columns — generate 1 test page FIRST
7. Verify test page fully — all fields, no truncation, correct layout
8. Generate remaining 29 pages
9. Design all manual pages (see page order in canva/CANVA_MCP.md)
10. Export PDF Print Quality — US Letter → exports/Main_Workbook_US_Letter.pdf
11. Export PDF Print Quality — A4 → exports/Main_Workbook_A4.pdf

**Return trigger:** `Canva done, page count: [X]`

---

## HANDOFF-4 — Etsy + Gumroad — Go Live
**Status:** ⏳ PENDING
**When:** After exports/ ZIP is assembled by Claude Code

### ETSY SETUP
1. Create new digital listing
2. Upload: 30_Day_Life_Reset_Workbook_v1.zip
3. Price: $5.99 (launch week) — raise to $8.99 after 10 sales
4. Use the best title variant from listings/etsy_listing.md
5. Add all 13 tags from listings/etsy_listing.md
6. Upload 5 mockup images (cover flat lay, interior spread, habit tracker, phone mockup, bundle shot)
7. Set: instant digital download, auto-renew ON

### GUMROAD SETUP
1. New product → digital download
2. Upload ZIP
3. Price: $8.99 with Pay What You Want floor: $5
4. Enable email capture
5. Upload Quick_Start_Guide.pdf as a separate FREE listing (lead magnet)
6. Cross-link: mention free guide in Etsy description

**Return trigger:** `Live on both platforms. Etsy: [URL] Gumroad: [URL]`

---

## HANDOFF-5 — Post-Launch Check
**Status:** ⏳ PENDING
**When:** After first 10 sales
**Return trigger:** `First 10 sales done. Reviews: [X]. Top feedback: [Y]`
