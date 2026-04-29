# Caveman Mode & Token Economy Guide

## WHAT IS CAVEMAN MODE
Short stripped inputs — no articles, no filler — to save tokens on navigation.
Activate: type `caveman on`
Deactivate: type `caveman off`

## SAFE TO CAVEMAN (navigation only)
| Short input | Meaning |
|-------------|----------|
| `next` | Generate next chunk |
| `save` | Confirm save to file |
| `status` | Show PROGRESS.md |
| `redo d11 t1` | Fix Day 11 Task_1 |
| `redo d8 goal: [new text]` | Replace Day 8 Goal |
| `skip` | Skip minor issue, note in qa_log.md |
| `done` | Phase complete, update PROGRESS.md |

## NEVER CAVEMAN (precision required)
- Phase 2 opening content generation prompt
- Gemini 3.1 Pro audit prompt (in HANDOFFS.md) — uses HIGH thinking budget
- Listing copy prompts (Phase 6)
- Email sequence prompts (Phase 7)
- Any prompt containing behavioral rules or schema definitions

## TOKEN BUDGET ESTIMATES
| Phase | Task | Est. Tokens | Priority |
|-------|------|-------------|----------|
| 2 | 9 content chunks | ~45,000 | INVEST — biggest quality driver |
| 6 | Etsy + Gumroad listings | ~6,000 | INVEST — conversion driver |
| 7 | Email sequences | ~5,000 | INVEST — revenue driver |
| 3 | CSV export | ~3,000 | Efficient — pure formatting |
| 5 | Packaging + CHANGELOG | ~2,000 | Efficient |
| 8 | Review flywheel emails | ~4,000 | Invest — ranking driver |
| 2.5 | Applying Gemini 3.1 Pro fixes | ~3,000 | Efficient — targeted edits |
| 2.5b | Gemini 3.1 Pro LOW spot-check | ~1,000 | Optional — only if 5+ HIGH issues |

## TOKEN SAVING RULES
1. Type `next` between chunks — never explain yourself
2. Fix fields with: `redo d[N] [field]: [new text]` — never retype whole day
3. Confirm saves with: `save` — Claude Code handles the rest
4. Type `status` not 'can you show me where we are in the project'
5. Open every session with `status` — costs almost nothing, orients everything

## WHEN TO USE OPUS 4 (sparingly)
- A full week (7 days) has wrong tone after Gemini 3.1 Pro audit
- Listing copy isn't converting after 48 hours live
- Email open rate below 20% after first send
- Never for initial generation — always Sonnet 4.5 first
