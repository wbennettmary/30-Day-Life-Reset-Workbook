# Master Template Spec — Daily Page (Canva)

**Phase:** 4 — Canva Design
**Page type:** Daily page (Days 1–30, generated via Bulk Create)
**Page count using this template:** 30
**Build first, test once, then bulk-generate.**

---

## 1. Canvas

| Setting | Value |
|---|---|
| Page size | US Letter — 8.5 × 11 in |
| Orientation | Portrait |
| Bleed | 0.125 in (Canva: turn ON "Show print bleed" — even though digital-only, future-proofs print) |
| Safe margin | 0.5 in all sides |
| Background | Solid `#FAF8F6` |

> Build the template at US Letter first. After QA passes, use Canva's **Resize** to duplicate the design as A4 (210 × 297 mm) — Canva will rescale text boxes proportionally; check that the named placeholders survive the resize.

---

## 2. Color Palette (lock as Brand Kit before you start)

| Token | Hex | Use |
|---|---|---|
| Primary BG | `#FAF8F6` | Page background |
| Secondary BG | `#FAF9F7` | Optional inner card backgrounds |
| Warm accent | `#EFE8DF` | Bottom-zone reflection card |
| Sage green | `#848B6F` | Day number, accent rules, leaf icons |
| Text primary | `#333333` | Body copy |
| Text secondary | `#4D4D4D` | Captions, "Why It Works" body |

In Canva: **Brand → Brand Kit → Add color** for each. Name them exactly as above so they appear in dropdowns.

---

## 3. Typography

| Role | Font | Weight | Size | Tracking | Case |
|---|---|---|---|---|---|
| Day number ("DAY 01") | Montserrat | Light 300 | 14 pt | +200 | UPPER |
| Title | Montserrat | SemiBold 600 | 28 pt | 0 | Title Case |
| Goal | Inter | Regular 400 | 12 pt | 0 | Sentence case |
| Section labels (TASKS / QUICK WIN / etc.) | Montserrat | Medium 500 | 9 pt | +300 | UPPER |
| Body (tasks, why, reflection, tomorrow) | Inter | Regular 400 | 11 pt | 0 | Sentence case |
| Mood scale row (literal text) | Inter | Regular 400 | 18 pt | +100 | — |
| Decorative subhead (optional) | A thin serif (e.g. Cormorant Garamond Italic) | Regular | 10 pt | 0 | Sentence case |

> Body line height: 1.4. Do NOT center-align body. Left-align tasks; center-align titles and the mood row only.

---

## 4. Layout Grid (US Letter — 8.5 × 11 in)

```
┌─────────────────────────────────────────────────┐  0.0 in
│  0.5 in margin                                  │
│  ┌─ TOP ZONE — 15% (1.65 in tall) ───────────┐  │
│  │  DAY 01                          (sage)   │  │
│  │  Title                           (lg)     │  │
│  │  ─────────────                 (sage rule)│  │
│  │  Goal: one sentence              (sm)     │  │
│  └────────────────────────────────────────────┘  │
│                                                 │
│  ┌─ MIDDLE ZONE — 60% (6.6 in tall) ──────────┐  │
│  │  TASKS                                    │  │
│  │   1. Task_1                                │  │
│  │   2. Task_2                                │  │
│  │   3. Task_3                                │  │
│  │                                           │  │
│  │  QUICK WIN          [leaf icon]           │  │
│  │   Quick_Win                                │  │
│  │                                           │  │
│  │  WHY IT WORKS                             │  │
│  │   Why_It_Works                             │  │
│  └────────────────────────────────────────────┘  │
│                                                 │
│  ┌─ BOTTOM ZONE — 25% (2.75 in tall) ─────────┐  │
│  │  ┌─ warm card (#EFE8DF, 12 px radius) ──┐ │  │
│  │  │ MOOD CHECK                          │ │  │
│  │  │ 😊 / 😐 / 😔   (literal, fixed)     │ │  │
│  │  │                                      │ │  │
│  │  │ REFLECTION                          │ │  │
│  │  │ Reflection                           │ │  │
│  │  │                                      │ │  │
│  │  │ TOMORROW → Tomorrow_Focus            │ │  │
│  │  └──────────────────────────────────────┘ │  │
│  └────────────────────────────────────────────┘  │
│  0.5 in margin                                  │
└─────────────────────────────────────────────────┘ 11.0 in
```

Zone heights (after margins): top ~1.5 in, middle ~6.0 in, bottom ~2.5 in.

---

## 5. Named Text Boxes — EXACT NAMES (Canva Bulk Create maps by these)

Place each as a separate Canva **Text** object. Right-click the text → **Edit data** → set the variable name to one of the names below (Canva uses the curly-brace syntax automatically when bound):

| Placeholder name | Required width | Recommended max characters | Dummy content for build |
|---|---|---|---|
| `{Day_Number}` | 1.5 in | "30" (2 chars) | `1` |
| `{Title}` | 6 in | 60 | `Day 1: Check In With Yourself` |
| `{Goal}` | 7 in | 200 | `Notice how you actually feel right now — without trying to fix anything.` |
| `{Task_1}` | 7 in | 200 | `Set a 5-minute timer and sit quietly without your phone.` |
| `{Task_2}` | 7 in | 200 | `Write 3 words that describe how you've been feeling lately.` |
| `{Task_3}` | 7 in | 200 | `Write one word for how you want to feel by the end of these 30 days.` |
| `{Quick_Win}` | 7 in | 200 | `Take 3 slow breaths before you do anything else today.` |
| `{Why_It_Works}` | 7 in | 200 | `Naming emotions reduces their intensity — affect labeling.` |
| `{Reflection}` | 7 in | 200 | `What's one thing you've been carrying that you haven't said out loud?` |
| `{Tomorrow_Focus}` | 6.5 in | 200 | `Tomorrow is about your mornings — notice how you wake up.` |

### Mood_Scale — DO NOT BIND TO CSV

`😊 / 😐 / 😔` is a **fixed text element**, not a placeholder. Type it once into the master template. Canva Bulk Create renders all 30 pages with this same literal element — exactly what we want.

> If you accidentally name a Mood_Scale placeholder, Canva will look for that column and either fail or render the literal string from each row, which can corrupt the emoji depending on font fallback. Keep it as plain text.

---

## 6. Decorative Elements

- **Sage divider rule** under the title: 1 px, `#848B6F`, 4 in wide, centered.
- **Leaf accent** beside "QUICK WIN" label: simple botanical line icon, sage `#848B6F`, ~16 px tall.
  - Use Canva search "single leaf line" — pick a minimal one-stem option, no fill.
- **Top corner sprig** (optional, top-right): same leaf icon at 24 px, rotated −20°.
- **No bold geometric patterns. No colored boxes. No drop shadows.** Breathing room IS the design.

---

## 7. Rounded Corners

- All cards/boxes: `12 px` corner radius.
- Bottom warm card (`#EFE8DF`): `16 px` radius.

---

## 8. Build Order (do this exactly once)

1. New Canva design → US Letter → blank.
2. Apply background `#FAF8F6` to the page.
3. Set up Brand Kit colors (section 2).
4. Place top zone: Day Number, Title, sage rule, Goal — using dummy content from section 5.
5. Place middle zone: section labels (TASKS / QUICK WIN / WHY IT WORKS) and three task lines, quick-win line, why-it-works line.
6. Place the warm bottom card (`#EFE8DF`, 16 px radius) and inside it: MOOD CHECK + literal `😊 / 😐 / 😔` + REFLECTION block + TOMORROW → block.
7. Add the leaf icon and optional top sprig.
8. **Now bind the placeholders.** Click each text element that should change per row → right-click → Bulk Create → Connect data → use the names from section 5.
9. Save the design as: **`30DLR — Master Daily Template`**.
10. Move to `02_bulk_create_guide.md` for the test-and-generate flow.

---

## 9. Pre-Bulk-Create Checklist (run before uploading CSV)

- [ ] Background is `#FAF8F6`
- [ ] All 10 placeholders named exactly as in section 5 — case-sensitive, underscores not spaces
- [ ] `Mood_Scale` is literal text, NOT a placeholder
- [ ] Page is US Letter portrait, not A4
- [ ] No banned-words leaked into dummy content (transform, journey, unlock, level up, optimize, hack, dominate, crush, supercharge)
- [ ] Title and Goal text boxes auto-fit ENABLED so longer days don't overflow
- [ ] Brand Kit colors locked
- [ ] Design saved with the exact name from build step 9

If all 8 boxes are checked, you are clear to run Bulk Create on a single test row.
