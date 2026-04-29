# Model Stack — 30-Day Life Reset Workbook
## Updated: April 2026

## CONFIRMED LIVE MODELS

### Gemini 3 Flash — `gemini-3-flash-preview`
**Role:** Environment setup, low-complexity structured tasks
**Thinking:** OFF
**Use for:** Creating files, updating configs, structured JSON tasks
**NOT for:** Behavioral content, creative writing, audit tasks
**Cost:** Lowest tier

### Gemini 3.1 Pro — High Thinking — `gemini-3.1-pro-preview`
**Role:** Full manuscript behavioral audit (HANDOFF-2)
**Thinking budget:** HIGH
**How to set:** In AI Studio → model settings → thinking budget → maximum
**Use for:** Reading all 9 chunks at once (1M context), catching every pacing/tone/schema issue
**NOT for:** Quick checks, file creation, anything under 10,000 tokens
**Cost:** Highest — used ONCE in the entire project
**When:** After all 9 chunks are saved in content/raw/

### Gemini 3.1 Pro — Low Thinking — `gemini-3.1-pro-preview`
**Role:** Spot-check verification after fixes applied
**Thinking budget:** LOW
**How to set:** In AI Studio → model settings → thinking budget → minimum
**Use for:** Verifying specific days after Claude applies fixes, quick targeted checks
**NOT for:** Full manuscript read — that needs High thinking
**Cost:** Medium — use only for targeted verification
**When:** After Claude Code applies Gemini audit fixes — verify 3-5 specific days only

### Claude Sonnet 4.5 — `claude-sonnet-4-5`
**Role:** Main content workhorse — everything Claude Code does
**Use for:** All 9 content chunks, CSV export, Etsy listing, Gumroad landing, all emails
**Cost:** Medium
**When:** Phases 2, 3, 5, 6, 7, 8

### Claude Opus 4 — `claude-opus-4`
**Role:** Surgical rewrites ONLY — escalation path
**Use for:** A full week that fails audit after two rounds, listing copy that isn't converting
**NEVER for:** Initial content generation (costs 5x Sonnet for same output)
**When:** Only on explicit escalation trigger

### ChatGPT Images 2.0
**Role:** Front and back cover PNG generation
**Use for:** HANDOFF-1 only
**When:** Before Phase 2 starts — covers must exist before content

### Canva MCP
**Role:** Design production
**Use for:** Bulk Create 30 daily pages, manual design all other pages
**When:** HANDOFF-3 after csv/daily_pages.csv is verified

---

## HOW TO SET THINKING BUDGET IN AI STUDIO
1. Go to aistudio.google.com
2. Select model: gemini-3.1-pro-preview
3. Click "Advanced settings" or the gear icon
4. Find "Thinking budget" slider
5. HIGH = slide to maximum (full audit — HANDOFF-2)
6. LOW = slide to minimum (spot-check verification)

## THINKING BUDGET: HIGH vs LOW — WHEN TO USE EACH

| Task | Budget | Reason |
|------|--------|--------|
| Full 9-chunk audit (HANDOFF-2) | HIGH | Needs deep reasoning across 80,000+ tokens |
| Verify Day 11 after fix | LOW | Single page check, no deep reasoning needed |
| Check if Week 2 has 3+ new behaviors | LOW | Targeted, specific, fast |
| Audit tone violations across full manuscript | HIGH | Requires holding whole document in reasoning |
| Spot-check one checkpoint page | LOW | Quick and cheap |

## COST CONTROL RULES
- Gemini 3.1 Pro High: use ONCE for the full audit. Never run it again unless content changes massively.
- Gemini 3.1 Pro Low: max 3 spot-check sessions. Each session: check max 5 specific days.
- Claude Opus 4: zero uses unless explicitly escalated. Always try Sonnet fix first.
- Between chunks: type `next` — 4 tokens, not 40.
