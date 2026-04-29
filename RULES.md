# Hard Rules — Claude Code Must Enforce These Always

## QUALITY GATE (run silently before every output)
```
[ ] No banned words: transform, journey, unlock, level up, optimize, hack, dominate, crush, supercharge
[ ] All 11 daily schema fields present in every day entry
[ ] Every field under 200 characters (count if unsure)
[ ] Every task concretely under 10 minutes
[ ] Mood_Scale exactly: 😊 / 😐 / 😔 — no variations
[ ] No line breaks inside any field
[ ] Behavioral pacing correct for the week (see CONTEXT.md)
[ ] Motivation touchpoint present if day is 1, 3, 10, 17, 24, or 30
[ ] Missed-day reset note present if day is 8, 15, or 22
[ ] Emotional arc matches week number
```
If any check fails → self-correct silently before outputting.

## OUTPUT FORMATS

### Chunk output format (Phase 2)
Every chunk saved to content/raw/chunk_0X.md
Structure:
```
# CHUNK [N] — [Section Name]
## Status: DRAFT
## Generated: [timestamp]
---
[full content]
---
## End Chunk [N]
```

### Daily page format inside chunks
```
### Day [N]: [Title]
**Goal:** [max 200 chars]
**Task 1:** [concrete action, max 10 min, max 200 chars]
**Task 2:** [concrete action, max 10 min, max 200 chars]
**Task 3:** [concrete action, max 10 min, max 200 chars]
**Quick Win:** [1-2 min action, max 200 chars]
**Why It Works:** [1 line behavioral science, max 200 chars]
**Reflection:** [1 journal prompt, max 200 chars]
**Mood:** 😊 / 😐 / 😔
**Tomorrow:** [1 sentence, max 200 chars]
```

### Step card format (show after every completed chunk or phase)
```
╔══════════════════════════════════════════╗
║  ✅ [CHUNK X / PHASE X] COMPLETE         ║
╠══════════════════════════════════════════╣
║  SAVED TO : [exact filepath]             ║
║  NEXT     : [what comes next]            ║
║  MODEL    : [which model for next step]  ║
║  CAVEMAN  : [ON or OFF]                  ║
║  ACTION   : type 'next' OR see HANDOFF   ║
╚══════════════════════════════════════════╝
```

### Model switch notification format
```
🔄 MODEL SWITCH REQUIRED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FROM : Claude Code (claude-sonnet-4-5)
TO   : [exact tool + model name]
WHY  : [one sentence]
DO   : [numbered steps]
RETURN WITH: "[exact trigger phrase]"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Handoff card format
```
🛑 HANDOFF-[N] — [Tool Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT   : [what needs to happen]
WHERE  : [exact tool and location]
STEPS  : [numbered, specific]
RETURN : "[exact trigger phrase to say when done]"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Waiting... Do not continue until trigger phrase received.
```

## CSV HARD RULES (Phase 3)
- Output raw CSV in a single code block — no preamble, no explanation
- 31 lines exactly: 1 header row + 30 data rows
- Headers exactly: Day_Number,Title,Goal,Task_1,Task_2,Task_3,Quick_Win,Why_It_Works,Reflection,Mood_Scale,Tomorrow_Focus
- Mood_Scale every row: 😊 / 😐 / 😔
- No line breaks inside fields
- Commas inside fields: wrap in double quotes

## FILE SAVING RULES
- Save every chunk immediately after generation — do not batch
- Update PROGRESS.md after every completed task
- Never overwrite a _final.md file with a draft
- CSV saved to: csv/daily_pages.csv
- Listings saved to: listings/
- Emails saved to: emails/

## CAVEMAN MODE RULES
ON  → Accept: 'next', 'save', 'redo d11 t1', 'status', short fixes
OFF → Full language for all prompts and phase openers

AUTO caveman ON: between-chunk navigation
NEVER caveman: opening prompts, audit prompts, listing/email prompts
