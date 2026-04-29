# Canva MCP Integration Guide — Phase 4
## Models used in this phase: Canva MCP (design) — no Gemini or Claude needed

## OVERVIEW
Canva MCP server in Antigravity allows Claude Code to interact with Canva directly.
Use it to automate repetitive design tasks while you handle layout decisions.

## WHAT CLAUDE CODE CAN DO VIA CANVA MCP
- Upload files (CSV, images) to Canva
- Trigger Bulk Create with a CSV
- List existing designs
- Export/download completed designs

## WHAT YOU STILL DO MANUALLY IN CANVA
- Build the master daily page template (text box placement, naming, styling)
- Design all non-daily pages (cover, week dividers, checkpoints, trackers, bonuses)
- Verify the test page before bulk generating all 30
- Assemble final page order
- Set export quality settings

## CANVA MCP WORKFLOW FOR PHASE 4

### Step 1 — Claude Code uploads CSV
```
Claude Code via MCP: upload csv/daily_pages.csv to Canva
```

### Step 2 — You build master template manually in Canva
Text box names (exact — Canva Bulk Create maps to these):
- {Day_Number}
- {Title}
- {Goal}
- {Task_1}
- {Task_2}
- {Task_3}
- {Quick_Win}
- {Why_It_Works}
- {Reflection}
- {Tomorrow_Focus}
Mood_Scale: Fixed text element — 😊 / 😐 / 😔 — NOT bound to CSV

### Step 3 — You run Bulk Create in Canva UI
1. Open your master template
2. Apps → Bulk Create → Upload Data
3. Select daily_pages.csv
4. Map columns to text boxes
5. Generate — TEST WITH 1 ROW FIRST
6. Verify test page fully before generating 30

### Step 4 — Claude Code exports via MCP (if supported)
```
Claude Code via MCP: export design as PDF, print quality, US Letter
Save to: exports/Main_Workbook_US_Letter.pdf
```

## DESIGN SYSTEM REFERENCE
```
Colors:
  Primary BG:  #FAF8F6
  Secondary BG: #FAF9F7
  Warm accent: #EFE8DF
  Sage green:  #848B6F
  Text:        #333333

Fonts:
  Header: Montserrat Regular, all-caps for RESET only
  Body: Inter or Helvetica Neue
  Accent: thin delicate serif or organic script

Layout grid (daily page):
  Top 15%:    Day number + Title + Goal
  Middle 60%: Tasks + Quick Win + Why It Works
  Bottom 25%: Mood + Reflection + Tomorrow Focus
```

## PAGE ORDER (56 pages total)
```
01. Front Cover (import covers/front_cover.png)
02. Quick Start
03. Why You Feel Stuck
04. How to Use
05. Life Audit
06. 90-Day Vision + 30-Day Focus
07. Week 1 Overview
08-14. Days 1-7 (Bulk Create)
15. Day 7 Checkpoint
16. Week 2 Overview
17-23. Days 8-14 (Bulk Create)
24. Day 14 Checkpoint
25. Week 3 Overview
26-32. Days 15-21 (Bulk Create)
33. Day 21 Checkpoint
34. Week 4 Overview
35-43. Days 22-30 (Bulk Create)
44. Day 30 Checkpoint
45. Monthly Habit Tracker Grid
46. Mood Tracker
47. Weekly Review Template
48-52. Category Trackers x5
53. Bonus: 50 Tiny Habits
54. Bonus: 7-Day Emergency Reset
55. Bonus: 90-Day Roadmap
56. Back Cover (import covers/back_cover.png)
```
