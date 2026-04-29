# GEMINI PROMPT — 30-Day Life Reset Workbook PDF Generator
# Paste this entire prompt into Gemini 2.5 Pro (1M context window).
# Ask it to write the complete Python script. Then run the script.
# Expected output: a production-ready 56-page PDF ebook.

---

## ═══════════════════════════════════════════════════════
## START OF PROMPT — COPY EVERYTHING BELOW THIS LINE
## ═══════════════════════════════════════════════════════

You are an expert Python developer and professional ebook/PDF designer. Your task is to write a **single, complete, immediately runnable Python script** that generates a full 56-page printable workbook PDF called the **30-Day Life Reset Workbook**.

Do not explain. Do not add caveats. Write the full script from start to finish. Every page. Every element. No placeholders, no "# TODO" comments, no "add content here" shortcuts. The script must run with `python generate_workbook.py` and produce a file called `30_Day_Life_Reset_Workbook.pdf`.

---

## SECTION 1 — TECHNICAL REQUIREMENTS

**Library:** Use `reportlab` only. Install with: `pip install reportlab`

**Font strategy:**
- Download Montserrat and Inter fonts from Google Fonts CDN at script start using `urllib.request`
- Register them with `pdfmetrics.registerFont` and `TTFont`
- Font files to fetch:
  - Montserrat-Light.ttf → https://fonts.gstatic.com/s/montserrat/v26/JTUSjIg1_i6t8kCHKm459WlhyyTh89Y.woff2 *(fallback: fetch from a reliable CDN)*
  - Actually: use the approach of downloading from Google Fonts API or jsDelivr CDN
  - **Simpler fallback that always works:** At the top of the script, try to import the TTF files. If they aren't found locally, use ReportLab built-in fonts as substitutes:
    - Montserrat-Light → `Helvetica`
    - Montserrat-SemiBold → `Helvetica-Bold`
    - Inter-Regular → `Helvetica`
    - Cormorant Garamond Italic → `Times-Italic`
  - Write a helper function `get_font(name)` that returns the registered font name or the fallback

**Page size:** `letter` (8.5 × 11 inches = 612 × 792 points)

**Units:** All measurements in points (1 inch = 72 points). Use a `MARGIN = 36` constant (0.5 inch).

**Canvas approach:** Use `canvas.Canvas` with `pagesize=letter`. Call `c.showPage()` between pages. Save with `c.save()`.

**Output file:** `30_Day_Life_Reset_Workbook.pdf` in the same directory as the script.

---

## SECTION 2 — DESIGN SYSTEM (apply to every page, no exceptions)

### Colors (RGB 0–1 scale)

```python
COLOR_BG         = (250/255, 248/255, 246/255)  # #FAF8F6 — page background
COLOR_BG2        = (250/255, 249/255, 247/255)  # #FAF9F7 — secondary background
COLOR_WARM       = (239/255, 232/255, 223/255)  # #EFE8DF — warm card background
COLOR_SAGE       = (132/255, 139/255, 111/255)  # #848B6F — sage green accent
COLOR_TEXT       = ( 51/255,  51/255,  51/255)  # #333333 — primary text
COLOR_TEXT2      = ( 77/255,  77/255,  77/255)  # #4D4D4D — secondary text
COLOR_WHITE      = (1, 1, 1)
```

### Typography scale

| Role | Font | Size (pt) | Case |
|------|------|-----------|------|
| Micro-label (DAY XX, WEEK N) | Montserrat-Light | 10 | ALL CAPS |
| Section label (TASKS, WHY IT WORKS) | Montserrat-SemiBold | 8 | ALL CAPS |
| Page title | Montserrat-SemiBold | 24 | Title Case |
| Large title (covers, week pages) | Montserrat-SemiBold | 28 | Title Case |
| Body text | Inter-Regular | 10.5 | Sentence case |
| Small body / captions | Inter-Regular | 9.5 | Sentence case |
| Accent italic quote | Times-Italic | 10 | Sentence case |

**Line height:** body = 1.4 × font size. Alignment: titles centered; all body text left-aligned.

### Layout constants

```python
PAGE_W, PAGE_H = 612, 792
MARGIN = 36          # 0.5 inch
CONTENT_W = PAGE_W - 2 * MARGIN   # 540 pt
CONTENT_H = PAGE_H - 2 * MARGIN   # 720 pt
```

### Rounded rectangle helper

Write a reusable function:
```python
def rounded_rect(c, x, y, w, h, r, fill_color, stroke=False):
    """Draw a filled rounded rectangle. y is bottom-left corner."""
    c.setFillColorRGB(*fill_color)
    if stroke:
        c.setStrokeColorRGB(*COLOR_SAGE)
        c.setLineWidth(0.5)
    c.roundRect(x, y, w, h, r, stroke=int(stroke), fill=1)
```

### Sage horizontal rule helper

```python
def sage_rule(c, x, y, width=200):
    c.setStrokeColorRGB(*COLOR_SAGE)
    c.setLineWidth(0.75)
    c.line(x, y, x + width, y)
```

### Writing line helper (for fill-in fields)

```python
def writing_lines(c, x, y, width, count=1, spacing=18):
    """Draw `count` thin underline writing lines."""
    c.setStrokeColorRGB(0.75, 0.75, 0.75)
    c.setLineWidth(0.4)
    for i in range(count):
        c.line(x, y - i * spacing, x + width, y - i * spacing)
```

### Page background

Every page starts with:
```python
c.setFillColorRGB(*COLOR_BG)
c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
```

### Leaf accent (SVG-style drawn with ReportLab paths)

Draw a minimal botanical leaf using bezier curves in sage color. Create a reusable function `draw_leaf(c, x, y, size=12)` that draws a simple pointed oval leaf shape using `c.beginPath()`, `c.moveTo()`, `c.curveTo()`, `c.closePath()`, `c.fill()`. Place one leaf beside "QUICK WIN" labels on daily pages, and a small sprig (2–3 leaves) in the top-right corner of week overview and checkpoint pages.

---

## SECTION 3 — PAGE STRUCTURE (all 56 pages in order)

### PAGE 01 — Front Cover

- Full-bleed warm gradient background: fill the entire page with `COLOR_WARM`
- Add a large sage-colored decorative arc or botanical sprig illustration (drawn with bezier curves) in the top-right quadrant
- **Title block** (centered, vertically positioned at 55% from bottom):
  - Small label: "A 30-DAY GUIDED WORKBOOK" in Montserrat-Light 10pt, sage color, ALL CAPS, letter-spacing effect (use spaces between characters)
  - Main title: "Life Reset" in Montserrat-SemiBold 42pt, text color `#333333`, centered
  - Subtitle: "Small shifts. Real momentum. Your reset starts here." in Times-Italic 13pt, text secondary, centered
- Sage horizontal rule (150pt wide) centered below subtitle
- Bottom area (bottom 15%):
  - Small tagline: "30 days · One page a day · At your pace" in Helvetica 9pt, text secondary, centered
- No image import needed — all drawn elements

### PAGES 02–05 — Front Matter

**Page 02 — Welcome**
- Top: sage micro-label "WELCOME" centered
- Title: "Small shifts. Real momentum." (Montserrat-SemiBold 24pt, centered)
- Sage rule centered below title (120pt)
- Body text (Inter 10.5pt, left-aligned, MARGIN to MARGIN, line height 15pt):

> You picked this up because something feels off. Maybe you've been going through the motions, carrying more than you should, or just quietly wishing things were different. That feeling is real — and it makes sense.
>
> This workbook isn't here to fix you. You're not broken. It's here to give you a small, steady path back to yourself.
>
> Over the next 30 days, you'll take one focused step each day. Nothing dramatic. Nothing that requires you to overhaul your life overnight. Just small, concrete actions that build on each other — one at a time, at your pace.
>
> Some days will feel easy. Some won't. Both are fine. You don't need to be motivated every day — you just need to show up when you can.

- After body: accent italic quote in warm card (`COLOR_WARM`, rounded 12pt, padding 12pt):
  > *"Let's begin."*

**Page 03 — Why You Feel Stuck**
- Top: micro-label "BEFORE YOU START" sage, centered
- Title: "Why You Feel Stuck" (Montserrat-SemiBold 24pt, centered)
- Sage rule 120pt centered
- Body text (3 paragraphs):

> Feeling stuck isn't a personality flaw. It's what happens when you've been in survival mode long enough that forward motion starts to feel impossible.
>
> When life gets full — work, responsibilities, relationships, all of it at once — your brain shifts its energy toward managing, not growing. You stay in the loop of what's urgent and never quite get to what matters.
>
> The result? Days that blur together. A vague sense that you should be doing more, feeling more, being more. And a creeping exhaustion that has nothing to do with sleep.
>
> Here's what actually helps: not a bigger plan, but a smaller one. Not more willpower, but better structure. Not a dramatic reset, but a gentle one. That's what the next 30 days are designed to give you.

- Closing italic pull-quote with sage rules above and below:
  > *"This isn't a flaw. It's a signal."*

**Page 04 — How to Use This Workbook**
- Title: "How to Use This Workbook"
- Intro line: "Each day has its own page. You'll find:" (body text)
- 7 bullet points with sage leaf bullets (draw a tiny 6pt leaf as bullet):
  - A daily goal — one clear intention for the day
  - Three tasks — each takes 10 minutes or less
  - A quick win — something you can do in 1–2 minutes to build momentum
  - Why it works — one sentence on the science behind the action
  - A reflection prompt — a single question to help you process the day
  - A mood check — just circle how you're feeling
  - Tomorrow focus — a one-line preview to prime your next day
- Warm card (`COLOR_WARM`, rounded 16pt) with text:
  > "You don't need to complete every item every day. Do what you can. Come back to what you missed when you're ready."
- Bold reminder line:
  > **One rule:** don't skip the reflection. Even one sentence counts. Writing is how this becomes yours.

**Page 05 — Quick Start**
- Title: "Quick Start" (large, 28pt, centered)
- Subtitle: "If you want to begin right now — here's your starting point." (italic, centered)
- Sage rule 150pt centered
- Three large numbered steps. Each number in sage color (36pt Montserrat-SemiBold), body text beside it:
  - **1** — Flip to Day 1. Read the goal and tasks.
  - **2** — Pick just one task. Do it today. One is enough.
  - **3** — Before bed, answer the reflection question. Even a few words.
- Warm closing card:
  > "You've started. That's the whole win for Day 1. Don't read ahead. Trust the structure — it was built with your pace in mind."
- Footer (bottom 10%): "See you on Day 1." — in sage, italic, centered

---

### PAGES 06–08 — Setup Pages

**Page 06 — Life Audit**
- Title: "Life Audit" (24pt centered)
- Subtitle italic: "Where you are right now — without judgment."
- Sage rule 120pt centered
- Intro line: "Rate each area from 1 to 5. Circle your number. 1 = struggling · 5 = solid"
- 8 rows in a structured layout. For each row:
  - Left: life area name (body bold, 10.5pt)
  - Center: "1  2  3  4  5" in sage color with small open circles drawn around each number
  - Right: "One word: ___________" writing line
  - Row divider: thin sage rule full width

  Rows:
  1. Energy & Sleep
  2. Work / Purpose
  3. Relationships
  4. Body & Movement
  5. Home & Space
  6. Mind & Stress
  7. Fun & Rest
  8. Finances (general)

- After table: two labeled writing fields:
  - "Your lowest two areas:" — 2 writing lines
  - "Your highest area (what's already working):" — 1 writing line
  - "One thing you've been avoiding:" — 1 writing line
- Warm card footer:
  > "You don't need to fix everything at once. This audit just helps you know where you're starting from — not where you should be."

**Page 07 — Your 90-Day Picture & 30-Day Focus**
- Two sections divided by a full-width sage rule at the midpoint

  **Top half — 90-DAY PICTURE**
  - Sage micro-label: "90-DAY PICTURE"
  - Title: "If things shift over the next 90 days, what changes?"
  - "In 90 days, I'd like to feel:" with a row of circled options: `Calmer · More rested · Clearer · More connected · Lighter · More like myself`
  - Writing fields: "One thing I'd like to have more of:" / "One thing I'd like to have less of:" / "If a friend described my life in 90 days, I'd want them to say:"

  **Bottom half — 30-DAY FOCUS**
  - Sage micro-label: "30-DAY FOCUS"
  - Title: "This month, I'm focusing on one thing."
  - Writing fields:
    - "My 30-day focus area:"
    - "One thing I'm going to start doing this month (small):"
    - "One thing I'm going to stop doing this month:"
    - "One thing I'm going to keep doing because it's working:"
    - "My personal 30-day intention (one sentence, your words):" — 2 lines

**Page 08 — Your Personal Reset Rules**
- Title: "Your Personal Reset Rules"
- Subtitle italic: "Three rules that make this work for you."
- Four sections with warm card styling around each:

  1. "I will try to show up:" — circle options: `Every day · Most days · Whenever I can`
  2. "If I miss a day, I will:" — 1 writing line
  3. "The time of day that works best for me:" — circle options: `Morning · Midday · Evening · No set time`
  4. "Who (if anyone) knows I'm doing this:" — 1 writing line
  5. "One thing I'm allowing myself to skip if needed:" — 1 writing line

- Footer card:
  > "Missing days is part of the process. What you do after a missed day matters more than the day you missed."
- Bold footer: "You're set up. Turn to Day 1."

---

### PAGE 09 — Week 1 Overview

- Background: `COLOR_BG`
- Top-right: draw sage leaf sprig (3 small leaves, 10–14pt each)
- Sage micro-label: "WEEK 1 · DAYS 1–7"
- Large title: "Foundation" (Montserrat-SemiBold 32pt, centered)
- Subtitle: "Energy & Awareness" (Times-Italic 14pt, centered, sage color)
- Sage rule 180pt centered
- Body text (3 short paragraphs):

> This week is light on purpose.
>
> You're not here to overhaul your routine or set big goals. You're here to notice — how you feel, what's draining you, and where there might be a little more room to breathe.
>
> Seven small days. Seven small steps. That's all.

- Warm card at bottom:
  > "Missed a day? That's the reset too. Pick up here."

---

### PAGES 10–16 — Days 1–7 (Daily Page Template)

**Daily page layout (apply identically to all 30 daily pages):**

The page has three vertical zones:

**TOP ZONE** (top 22% of content area = ~158pt tall):
- Sage micro-label left-aligned: "DAY [N]" (10pt Montserrat-Light, ALL CAPS)
- Title (Montserrat-SemiBold 22pt, left-aligned, wraps if needed)
- Sage rule (full content width, 1pt, sage color)
- Goal text (Inter 10.5pt italic, left-aligned): "Goal: [goal text]"

**MIDDLE ZONE** (next 53% = ~382pt tall):
- Section label "TASKS" (8pt Montserrat-SemiBold, ALL CAPS, sage color)
- Three numbered tasks (Inter 10.5pt, left-aligned, line height 15pt):
  ```
  1. [Task_1]
  2. [Task_2]
  3. [Task_3]
  ```
- 16pt gap
- Row with section label "QUICK WIN" + leaf icon (draw_leaf at sage color, 10pt):
  - Quick win text (Inter 10.5pt italic)
- 16pt gap
- Section label "WHY IT WORKS"
  - Why text (Inter 9.5pt, `COLOR_TEXT2`)

**BOTTOM ZONE** (bottom 25% = ~180pt):
Warm card (`COLOR_WARM`, 16pt radius, full content width, ~165pt tall):
- Inner content with 12pt padding on all sides:
  - Row: Section label "MOOD CHECK" + emoji row: `😊  /  😐  /  😔` (fixed, 14pt, centered)
  - Thin sage rule inside card (80%)
  - Section label "REFLECTION"
  - Reflection text (Inter 9.5pt italic): "[Reflection prompt]"
  - 2 writing lines (full warm-card inner width)
  - Thin sage rule
  - Row: "TOMORROW →" label (sage, 8pt bold) + Tomorrow_Focus text (Inter 9.5pt)

Use the CSV data below to populate all 30 daily pages.

---

### PAGES 17, 26, 35, 46 — Weekly Checkpoints

Apply the same layout to all four. Content differs per checkpoint.

**Layout:**
- Sage leaf sprig top-right
- Sage micro-label: "WEEK [N] CHECKPOINT"
- Title: "Week [N] Review" (24pt, centered)
- Sage rule 150pt centered
- Five fill-in sections, each with:
  - Bold label (8pt Montserrat-SemiBold, sage, ALL CAPS)
  - 2–3 writing lines
  - Thin divider line

Sections (for all four checkpoints):
1. "What worked this week?" — 3 lines
2. "What felt heavy or hard?" — 3 lines
3. "My one win from this week:" — 1 line + circle options: `Small win · Medium win · Bigger than I expected`
4. "My mood across this week:" — circle options: `Mostly 😊 · Mostly 😐 · Mostly 😔 · All over the place`
5. Restart permission warm card:
   - Week 1: "If you missed days, skipped tasks, or didn't fill in every page — that's fine. This isn't a test with a score. It's a reset, and resets are allowed to be imperfect. You're still in."
   - Week 2: "Week 2 is often where the newness wears off and the real test begins. If you struggled, that's not failure — that's the work. The habit you're building isn't the morning routine. It's the habit of returning. You returned. That's the one that matters."
   - Week 3: "Three weeks in. You may be tired. That's real. Tired doesn't mean failing — it means you've been doing the work. Week 4 is slower on purpose."
   - Week 4 / Final: "There will be a Day 31. And a Day 60. Life doesn't stop giving you hard stretches. But now you know what a re-entry looks like. When things get hard again — come back. Start small. One thing. That's all it's ever taken."
6. "One word for Week [N]:" — 1 writing line
7. "One word for what I want Week [N+1] to feel like:" — 1 writing line

---

### PAGE 18 — Week 2 Overview
- Sage micro-label: "WEEK 2 · DAYS 8–14"
- Title: "Momentum" (32pt)
- Subtitle: "Habits & Productivity" (italic 14pt sage)
- Body:
  > Week 2 is where things get real. The novelty of starting is behind you — now you build.
  >
  > This week you'll experiment with one morning habit, learn how to make it stick, and check in honestly with how it's going. No pressure to be perfect. Flexible consistency beats rigid willpower every time.
  >
  > Small wins add up more than you think.
- Warm card: "Missed a day? That's the reset too. Pick up here."

### PAGE 27 — Week 3 Overview
- Sage micro-label: "WEEK 3 · DAYS 15–21"
- Title: "Growth" (32pt)
- Subtitle: "Body, Mind, Environment" (italic 14pt sage)
- Body:
  > Week 3 is about your surroundings — internal and external. You'll add movement, clear mental clutter, and take one more look at your physical space.
  >
  > This isn't a productivity sprint. It's a slow expansion — noticing what you're carrying, and setting a little of it down.
  >
  > Progress, not perfection.
- Warm card: "Missed a day? That's the reset too. Pick up here."

### PAGE 36 — Week 4 Overview
- Sage micro-label: "WEEK 4 · DAYS 22–30"
- Title: "Integration" (32pt)
- Subtitle: "Identity, Values, Future" (italic 14pt sage)
- Body:
  > Week 4 asks the bigger questions. Not what you're doing — but who you're becoming.
  >
  > This week is quieter. The tasks are smaller. You'll name your values, look at the life you're building, and make one real commitment for what comes after Day 30.
  >
  > You've got this.
- Warm card: "Missed a day? That's the reset too. Pick up here."

---

### PAGES 47–54 — Trackers Section

**Page 47 — 30-Day Habit Tracker Grid**
- Title: "Habit Tracker" (24pt)
- Subtitle: "Track up to 6 habits across all 30 days. Fill the box each day you complete it."
- Header row: "Habit →" + 6 columns with underline fields for habit names
- 30 data rows (Day 1–30) + Total row
- Each cell: small open square `□` (draw with `c.rect`, 8×8pt, no fill, sage stroke)
- Row dividers: thin lines (0.3pt)
- Footer: "Consistency doesn't mean every box. It means most of them, most of the time."

**Page 48 — 30-Day Mood Log**
- Title: "Mood Tracker"
- Subtitle: "One circle per day. No analysis needed — just mark what's true."
- 4-week grid (7 columns Mon–Sun, 4 rows)
- Each cell contains: "😊  😐  😔" — reader circles one
- Below grid: writing fields for pattern reflection
- Footer: "There are no wrong moods."

**Page 49 — Weekly Review Template**
- Title: "Weekly Review"
- Subtitle: "Use this page once per week. Photocopy or duplicate as needed."
- 4 sections (Week 1–4) each with:
  - Week number label
  - "Days I showed up: ___ out of 7"
  - 3 short writing prompts with lines
  - Energy circle: `Low · Medium · High · Variable`
  - Thin divider

**Page 50 — Health & Body Tracker**
- Title: "Health & Body"
- 4-column weekly grid (Week 1–4) with rows:
  - Sleep quality (1–5)
  - Energy level (1–5)
  - Movement / activity (1–5)
  - Eating / nourishment (1–5)
  - Water intake (1–5)
  - Physical tension / pain (1–5)
- Writing fields: "One small health win this month:" / "One habit I want to keep for my body after Day 30:"

**Page 51 — Focus & Productivity Tracker**
- Title: "Focus & Productivity"
- 4-column grid with rows:
  - Felt focused (1–5)
  - Avoided distractions (1–5)
  - Got one important thing done (Yes/No circles)
  - Phone use felt intentional (Yes/No circles)
- Writing fields: reflection on what got done / attention habit to carry forward

**Page 52 — Home & Environment Tracker**
- Title: "Home & Environment"
- Table with columns: Area / Cleared? (Yes/No) / Week / Still to do?
- Rows: Desk / workspace · Bedroom · Kitchen counter · Bag/wallet/car · Digital clutter · Other
- Writing fields at bottom

**Page 53 — Money & Finances Tracker**
- Title: "Money & Finances"
- 4-column weekly grid with rows:
  - Felt in control of spending (1–5)
  - Had at least one unplanned purchase (Yes/No)
  - Checked account balance (Yes/No)
  - One money stress I'm carrying (short write-in)
- Writing fields: habit noticed / one thing to do differently

**Page 54 — Relationships & Connection Tracker**
- Title: "Relationships & Connection"
- 4-column weekly grid:
  - Felt connected to someone (1–5)
  - Had one real conversation (Yes/No)
  - Reached out to someone first (Yes/No)
  - Felt lonely at some point (Yes/No)
- Writing fields: relationship invested in / person to be more intentional with / what made you better to be around

---

### PAGES 55–57 — Bonus Pages

**Page 55 — 50 Tiny Habits**
- Title: "50 Tiny Habits"
- Subtitle italic: "All under 5 minutes. Pick one. Try it twice."
- Two-column layout (each column 250pt wide, 12pt gap)
- 6 categories, each with small sage open-circle bullets:

  **BODY & HEALTH (9):**
  1. Drink a full glass of water before you do anything else in the morning.
  2. Take 5 slow, deliberate breaths. Exhale longer than you inhale.
  3. Stretch for 2 minutes when you get out of bed — any movement counts.
  4. Go to bed 15 minutes earlier than usual tonight.
  5. Eat one piece of fruit or vegetable you wouldn't normally bother with.
  6. Walk around the block once. One loop, no destination required.
  7. Close your eyes for 60 seconds in the middle of the day.
  8. Open a window and get 2 minutes of fresh air.
  9. Take any supplements or medications you've been skipping. Right now.

  **MIND & MOOD (9):**
  10. Write 3 things that went okay today. Not great — just okay.
  11. Read one page of a book you've been meaning to start.
  12. Sit quietly for 2 minutes without a screen. Just sit.
  13. Write down one worry on paper, then close the notebook.
  14. Choose one word for how you want to feel today. Write it somewhere visible.
  15. Turn off all notifications for the next hour.
  16. Spend 5 minutes outside — not exercising, just being outside.
  17. Write one thing you're looking forward to, even if it's small.
  18. Notice one beautiful thing in your environment. Write it down.

  **FOCUS & PRODUCTIVITY (8):**
  19. Write your top 3 tasks for today on paper. Cross them off as you go.
  20. Clear your phone home screen of everything you don't need there.
  21. Set a 25-minute timer and work on one thing only until it goes off.
  22. Decline or defer one thing this week that isn't genuinely urgent.
  23. Make one small decision you've been putting off for more than a week.
  24. Prepare your bag, clothes, or desk the night before.
  25. Spend 5 minutes at end of day writing what you'll do first tomorrow.
  26. Check your email only at two set times today — not continuously.

  **HOME & ENVIRONMENT (8):**
  27. Clear one surface completely. Put back only what belongs.
  28. Make your bed within 10 minutes of getting up.
  29. Do the dishes immediately after eating.
  30. Put 5 objects back where they actually belong.
  31. Take out the trash or recycling before it overflows.
  32. Wipe down one kitchen or bathroom counter.
  33. Put away clean laundry within 24 hours of washing.
  34. Spend 3 minutes tidying the space where you spend most of your time.

  **MONEY & FINANCES (7):**
  35. Check your bank balance. Just look at the number.
  36. Cancel one subscription you haven't used in the last month.
  37. Make a list before your next grocery shop and stick to it.
  38. Unsubscribe from 3 promotional emails you never open.
  39. Pack or prep your own lunch once this week instead of buying it.
  40. Review one bill or recurring charge and confirm it's still worth it.
  41. Write down one purchase from this week you didn't need.

  **RELATIONSHIPS & CONNECTION (9):**
  42. Send a "thinking of you" message to someone you haven't contacted in a while.
  43. Reply to one message you've been putting off. One sentence is enough.
  44. Put your phone away completely for one meal today.
  45. Make eye contact and actually listen during your next conversation.
  46. Say thank you to someone with one specific detail: "thank you for ___."
  47. Call someone instead of texting them. Just once today.
  48. Remember and acknowledge one upcoming birthday for someone you care about.
  49. Ask someone how they're really doing — and wait for the real answer.
  50. Tell one person one specific thing you appreciate about them.

**Page 56 — 7-Day Emergency Reset**
- Title: "7-Day Emergency Reset"
- Subtitle: "When you need to start fast."
- 7 cells in a 1-column stacked layout (each cell ~85pt tall, warm card, 12pt radius):
  - Each cell has: **Day label** (sage, bold) + Task line + Reflection line + Quick Win line

  Day 1: Just Show Up — Task: Drink a full glass of water. Go to bed at a reasonable time. · Reflection: What happened? Write one honest sentence about why things derailed. · Quick Win: Read this page. You've already started.
  Day 2: One Familiar Thing — Task: Do one habit from your 30-day workbook — any one. · Reflection: What does it feel like to do one small thing on a hard day? · Quick Win: Set a reminder for the same time tomorrow.
  Day 3: Clear Something — Task: Spend 5 minutes clearing one small physical space. · Reflection: Did the space feel different after? · Quick Win: Wipe the surface down.
  Day 4: Empty Your Head — Task: Set a 5-minute timer and write everything in your head. · Reflection: Is there one thing you can actually do something about today? · Quick Win: Cross off one item.
  Day 5: Move — Task: Walk outside for 10 minutes. No phone. · Reflection: How did your body feel before vs. after? · Quick Win: Stretch for 60 seconds right now.
  Day 6: Name One Good Thing — Task: Write 3 things that are going okay right now. · Reflection: Why is it hard to notice what's okay when things are hard? · Quick Win: Say one of the three things out loud.
  Day 7: Come Back — Task: Read your original Day 1 reflection from the main workbook. · Reflection: What do you notice about the gap between Day 1 and right now? · Quick Win: Decide — go back to Day 1, or run another 7-day reset first.

- Footer warm card: "You made it through the hard part. Coming back is always the right call."

**Page 57 — 90-Day Continuation Roadmap**
- Title: "What Comes After Day 30"
- Subtitle italic: "Slow is sustainable. You've got this."
- Three stacked sections with sage dividers:

  **MONTH 2 — Deepen One Thing**
  - Body: "Pick the one habit from your 30 days that made the most difference. Your only job in Month 2 is to deepen it."
  - Writing fields: "Your Month 2 habit:" / "Frequency: Daily · Most days · Weekly" (circle)
  - "How you'll know it's working:" / "Your Month 2 check-in date:"
  - Checkbox list (six focus areas with open-circle checkbox):
    ○ Body & sleep · ○ Focus & productivity · ○ Environment · ○ Relationships · ○ Money · ○ Mind

  **MONTH 3 — Add One More**
  - Body: "Keep your Month 2 habit and add one new small behavior from the 50 Tiny Habits list."
  - Writing fields: "Your Month 3 new habit:" / "Why you chose it:" / "Your Month 3 check-in date:"

  **YOUR 90-DAY PERSONAL CHECK-IN**
  - Body: "Fill this in at Day 90 — approximately 3 months from when you started."
  - Writing fields: "What I kept from the 30 days:" / "What I let go of:" / "One thing about my life that's different now:" / "Word for the last 90 days:" / "Word for the next 90:"

- Footer: "> You don't need to figure out the whole year. Just the next 90 days. Then the next. That's enough."

---

## SECTION 4 — COMPLETE DAILY PAGE CONTENT (CSV DATA)

Use the following data for Pages 10–16 (Days 1–7), 19–25 (Days 8–14), 28–34 (Days 15–21), 37–45 (Days 22–30).

```
Day | Title | Goal | Task_1 | Task_2 | Task_3 | Quick_Win | Why_It_Works | Reflection | Tomorrow_Focus
1 | Day 1: Check In With Yourself | Notice how you actually feel right now — without trying to fix anything. | Set a 5-minute timer and sit quietly without your phone. Notice thoughts and body tension. | Write 3 words that describe how you've been feeling lately. No editing — just what's true. | Write one word for how you want to feel by the end of these 30 days. Put it somewhere visible. | Take 3 slow breaths before you do anything else today. | Naming emotions reduces their intensity — a well-documented effect called affect labeling. | What's one thing you've been carrying lately that you haven't said out loud to anyone? | Tomorrow is about your mornings — notice how you wake up and how you feel in the first 10 minutes.
2 | Day 2: Your Morning Signal | Notice what your mornings feel like before you change anything about them. | When you wake up tomorrow notice the very first thought in your head. Write it down before anything else. | Write down the first thing you typically do each morning and honestly note how it makes you feel. | Close your eyes and picture tomorrow morning going well. Write one word for how you want it to feel. | Set your phone across the room tonight so tomorrow's start is a little calmer. | Morning routines activate the brain's planning circuits making the rest of the day feel more manageable. | What does a good morning feel like to you? What would need to be true for that to happen more often? | Tomorrow you'll notice one small thing that's been quietly draining your energy.
3 | Day 3: One Good Thing | Find evidence that things aren't entirely wrong — even if the evidence is small. | Write down 3 things that went okay today. They don't have to be good — just okay is enough. | Think of one person who makes you feel steadier. Write one sentence about what it is about them. | Look around the space you're in right now and find one thing you actually like about it. | Name one thing that made you smile this week even briefly. Write it down. | Noticing small positives rewires attention patterns over time — a core principle in behavioral science. | What's one small thing that's been going right lately that you haven't given yourself credit for? | Tomorrow is about your physical space — one corner one drawer one surface.
4 | Day 4: Clear One Space | Create one small area that feels calm and a little more like yours. | Look around your space right now. Write one sentence about how the order or clutter makes you feel. | Put back only what belongs there. Everything else goes in a drawer a box or the bin. | Spend 2 minutes in that cleared space. Sit or stand there. Just notice how it feels different. | Wipe the surface down with a cloth. A clean space signals calm to your brain immediately. | Visual clutter competes for attention — removing it lowers background stress without any other effort. | Is there a space in your home that makes you feel tired just looking at it? What could you remove? | Tomorrow you'll track your energy at different times of day — no changes yet just noticing.
5 | Day 5: Your Energy Map | Notice when your energy rises and falls so you can work with it instead of against it. | At three points today — morning afternoon evening — pause and rate your energy 1–5. Write the numbers. | Look at what you wrote. When do you feel sharpest? When do you fade? Write one sentence about the pattern. | Write one sentence about when you feel most drained during the day and what usually seems to trigger it. | Drink a glass of water right now. Mild dehydration is one of the most common hidden energy drains. | Matching tasks to natural energy rhythms increases focus without requiring more willpower. | What do you usually do during your lowest-energy hour of the day? Is that working for you? | Tomorrow is about sleep — not fixing it yet just getting an honest picture of what's happening.
6 | Day 6: Your Sleep Reality | Get an honest picture of your sleep this week without judgment. | Write down your typical bedtime wake time and how rested you feel most mornings on a scale of 1–5. | Name one thing that regularly cuts into your sleep — screen time stress late eating noise. Just name it. | Write one sentence about how your current sleep quality affects how you feel and relate to people. | Turn on Do Not Disturb before you go to sleep tonight. | Sleep quality affects mood focus and appetite regulation more than almost any other single factor. | What would feel different in your daily life if you were consistently more rested? | Tomorrow wraps Week 1 — you'll look back at what you noticed and name one thing that already shifted.
7 | Day 7: Week 1 Wrap | Acknowledge what you've noticed this week and name one small thing that's already different. | Flip back through Days 1–6. Read what you wrote. Don't analyze — just notice what stands out. | Write one thing you noticed about yourself this week that surprised you or just felt true. | Write one thing you want to carry into Week 2 — a habit a thought or a small action that helped. | Put a mark or star on today's date somewhere visible — a sticky note journal or calendar. | Reflection consolidates learning. Reviewing what worked makes the behavior more likely to continue. | What's one thing you did this week however small that you're glad you did? | Week 2 starts tomorrow — it's about momentum. Small habits gently built one at a time.
8 | Day 8: Coming Back | Return to the workbook without guilt — whether you missed one day or several. | Read back over your Day 7 wrap. Remind yourself what you noticed. One minute no pressure. | Pick one task from any day you missed. Just one. Do that one thing today. | Write one honest sentence about what the last few days looked like. Just a note nothing more. | Refill your water and sit down for 2 quiet minutes before you do anything else today. | Returning after a gap without self-judgment is itself a skill — and one of the most valuable ones. | What made it hard to show up? Not to judge it — just to understand it. | Tomorrow you'll look at where your attention actually goes during the day — and whether that's by choice.
9 | Day 9: Where Your Attention Goes | Notice what you're spending time and attention on — without changing anything yet. | Pause and notice how your attention felt today. Scattered pulled around or mostly steady? Write one word. | Think about your last evening. What did you do for most of it? Write it down honestly. | Make two lists: what you gave attention to today and what you wish you'd given more attention to. | Put your phone face-down for the next 15 minutes. Just notice what that feels like. | Awareness of attention patterns is the first step to shifting them — without data any change is guesswork. | If a log showed everything you did this week would it match what you say matters to you? | Tomorrow is Day 10. You've made it nearly a third of the way through. That's worth pausing for.
10 | Day 10: Ten Days In | Pause and acknowledge that ten days of showing up is genuinely significant. | Go back to your Life Audit from the Setup Pages. Rate the same areas again. Notice any shifts. | Write one thing that feels even slightly easier or clearer than it did on Day 1. One thing is enough. | Write what you want Week 2 to focus on for you. Keep it to one area — morning routine sleep or focus. | Say out loud or write: "Ten days. I'm doing this." Mean it. | Mid-point reflection creates a psychological marker that increases follow-through in the second half. | What would you tell someone else who was at Day 10 and quietly doubting themselves? | Tomorrow you'll choose and start one morning habit. Small specific and entirely yours.
11 | Day 11: One Morning Habit | Choose one morning habit and start it today — no elaborate routine just one thing. | Choose your habit: drink water before coffee · 5 deep breaths after waking · write 3 lines in a notebook. | Write it down: "My morning habit this week is ___." Put it somewhere you'll see it when you wake up. | Do your habit right now or set a specific time tomorrow when you will. Commit to the time not the idea. | Set a phone reminder 10 minutes after your usual wake time. Label it with your habit name. | Attaching a new behavior to a fixed morning window builds consistency faster than waiting to feel motivated. | Why this habit? What do you hope it quietly gives you over time? | Tomorrow you'll attach your habit to something you already do — making it much harder to forget.
12 | Day 12: Stack It | Lock in your morning habit by pairing it with something you already do automatically. | Name your most automatic morning behavior — brewing coffee brushing teeth opening curtains. Write it down. | Write your habit stack: "After I [existing behavior] I will [new habit]." This is your cue. | Do the full stack this morning. Existing behavior then new habit. Back to back. Write one word about it. | Write the stack on a sticky note and place it where the cue happens — by the kettle sink or bedside. | Habit stacking uses existing neural pathways as triggers cutting the effort needed to start a new behavior. | What's one habit you already have that you never think about? What made it automatic over time? | Tomorrow you'll check honestly how the habit has been landing — without pressure on the result.
13 | Day 13: Honest Check-In | Assess how your morning habit is going — honestly without judging whatever the answer is. | Rate how consistently you did your morning habit this week from 1–5. Write the number and one reason. | Write what got in the way if anything — time energy forgetting resistance. Just name it clearly. | Adjust if needed. Simpler version? Different timing? Different habit? Write the updated version now. | Do your morning habit right now even if it's the afternoon. Timing matters less than keeping it going. | Flexible consistency — adapting without quitting — builds habits more reliably than all-or-nothing thinking. | What's the difference between a habit that's hard and a habit that's simply wrong for you right now? | Tomorrow wraps Week 2 — you'll note what shifted and decide what to carry into Week 3.
14 | Day 14: Week 2 Wrap | Acknowledge the habit work you did this week and decide what's worth carrying forward. | Write a short summary of Week 2. What did you try? What stuck? What didn't? Three to five sentences. | Decide: keep your morning habit into Week 3 adjust it or replace it with something that fits better. | Write one thing this week taught you about how you actually work — not about habits but about yourself. | Mark Day 14 on your tracker or calendar. Two weeks done. | Turning experience into a brief written summary helps the brain store it as a lesson rather than an event. | What made this week harder than Week 1? What made it more meaningful? | Week 3 starts tomorrow — body mind and environment. It's a noticeable shift. You're ready for it.
15 | Day 15: Coming Back Again | Return to the work without making a story out of the gap — or the time away. | Don't scroll back to calculate what you missed. Open to today start here and go forward from now. | Write one sentence about where you are right now — energy mood headspace. Just the honest current state. | Do your morning habit from Week 2 or your adjusted version. One familiar action to re-anchor. | Make yourself something warm to drink. Sit with it for 2 minutes. You're back. | Re-entry without self-criticism is a learnable skill. The brain returns more easily when the cost is low. | What made Week 3 harder to start than Week 1 or 2? What got in the way? | Tomorrow you'll add movement — 10 minutes nothing intense. Just your body briefly awake.
16 | Day 16: Move for 10 Minutes | Add one short daily movement — not for fitness just to feel more present in your body. | Walk outside for 10 minutes. No podcast no phone. Just walk slowly and look at what's around you. | When you're done write one word for how your body felt before the walk and one word for after. | Choose a specific time tomorrow you'll repeat this. Write it: "Tomorrow at [time] I'll walk 10 minutes." | Stand up and stretch for 60 seconds right now. Any stretch. Just move something. | Brief movement raises mood-regulating neurotransmitters and reduces tension faster than almost any habit. | When was the last time you moved your body without it being for a specific outcome or goal? | Tomorrow is the halfway point. You'll pause and take stock of how far you've actually come.
17 | Day 17: Halfway There | Mark the halfway point and let yourself genuinely feel what that means. | Write three things that are different from Day 1 — in how you feel think or act. Small differences count. | Go back to your 30-day intention from the Setup Pages. Read it. Write one word about how it lands now. | Write what you want the second half to feel like. Not a goal — just a feeling. One word or sentence. | Take a photo of today's date or write it somewhere. Halfway done is a real thing worth noting. | Naming progress at a milestone increases follow-through — the brain treats acknowledged effort as worth protecting. | What's one thing you've quietly let go of in the last 17 days even just a little? | Tomorrow you'll work on clearing mental clutter — the kind you can't see but definitely feel.
18 | Day 18: Clear Your Head | Reduce one source of mental clutter that's been running in the background without you choosing it. | Brain dump for 5 minutes — everything in your head right now. Worries tasks loops random thoughts. All out. | Read what you wrote. Circle one item that's actually within your control right now. Just one. | Take one small action on it — a reply a note a decision one concrete step. Keep it under 2 minutes. | Close 5 browser tabs or app windows you haven't touched in days. Small clears add up quickly. | Writing down mental load frees working memory and makes problems feel more contained and manageable. | What thought has been on repeat for you lately that you haven't actually addressed or resolved? | Tomorrow is about your physical environment — a deeper clear than what you did in Week 1.
19 | Day 19: Your Environment Continued | Improve one more corner of your physical space — building on the clear you did in Week 1. | Choose a different space from Day 4 — a drawer shelf car bag or closet section. Set a 7-minute timer. | Clear it out. Keep only what belongs works or you actually use. Bin donate or relocate the rest. | Take a photo of the cleared space. Look at it when you feel overwhelmed this week. | Empty one thing right now — a bag a pocket a small tray. 60 seconds flat. | Physical order measurably lowers cortisol — your nervous system responds directly to what your eyes take in. | Which area of your life feels most cluttered right now — physical space your mind or your relationships? | Tomorrow you'll take one step toward something you've been quietly putting off.
20 | Day 20: The Thing You've Been Avoiding | Get curious about one thing you've been circling around — without any pressure to start it today. | Write down the thing you've been avoiding. Don't plan it or judge it — just name it clearly on paper. | Write one honest sentence about why this thing has been waiting. What have you been telling yourself? | Write what it would feel like to have simply started it — not finished it just started. Notice what comes up. | Write: "The thing I've been circling is ___." Naming it clearly is itself a small act of honesty. | Understanding why we avoid something is often more useful than forcing a start before we're ready. | What's one small thing that would need to be true before starting this felt manageable to you? | Tomorrow wraps Week 3 — and starts asking bigger questions about what you actually want.
21 | Day 21: Week 3 Wrap | Take stock of what Week 3 built — in habits headspace and your sense of what's possible from here. | List the habit areas you've tried in the last three weeks — morning routine movement mental clarity. | Write one honest sentence about how you've shown up this month — the moments you're glad about. | Look ahead to Week 4. Write one question you want it to help you answer about your life. | Mark Day 21 on your tracker. Three weeks done. One left. | Shifting from reviewing behavior to examining identity is how temporary habits become lasting character. | What would you need to believe about yourself to keep going after this workbook ends? | Week 4 is the final stretch — identity values and a life you want to return to. It starts tomorrow.
22 | Day 22: Coming Back — Final Time | Return to this last week cleanly — whatever the gap whatever happened in between. | Write today's date and one word for how you're showing up right now. That's your entry point. | Read your Day 21 wrap. Find the question you wrote for Week 4. Read it once and let it settle. | Do your morning habit — just the one. Re-anchor with something familiar before this final week begins. | Take 3 slow breaths. You're in the last stretch. | Intentional re-entry signals that what follows matters creating the attention to finish well. | What would make this final week feel complete even if it doesn't go perfectly? | Tomorrow you'll name what actually matters to you — not what should but what genuinely does.
23 | Day 23: Your Values | Name two or three things that genuinely matter to you — not aspirationally but actually true right now. | Write a fast list of 10 things you care about. No editing — whatever surfaces first. Two minutes. | Circle the two or three that feel most true right now. Not most impressive. Most honest. | For each circled value finish the sentence: "This matters to me because ___." One sentence each. | Read your circled values out loud. Notice if any of them surprise you. | Named values act as a decision filter — they make future choices feel clearer and less draining over time. | Where in your current daily life do your actions most reflect what you actually value? | Tomorrow you'll connect those values to the life you've been quietly building this month.
24 | Day 24: The Life You're Building | Connect the small things you've been doing to a larger picture of the life you actually want. | Look at your values from yesterday. Write one way your daily life already reflects each one. | Write 3–5 sentences describing a regular day in your life six months from now. Keep it grounded. | Find one behavior from this workbook that connects to that picture. Write one sentence linking them. | Read your six-months description slowly as if reading about someone you genuinely admire. | Connecting current behavior to a specific future self increases follow-through more than willpower alone. | What's one thing you've started this month that the person in your six-month picture would recognize? | Tomorrow you'll look at what you're still carrying that doesn't fit that picture anymore.
25 | Day 25: What No Longer Fits | Identify one habit thought or pattern you're ready to leave behind — honestly and without drama. | Write 5 things you've been doing thinking or holding onto that don't match who you're becoming. | Circle the one that's costing you the most. Write one sentence about why you've held onto it this long. | Write one small action that signals to yourself that you're putting it down. Do it today. | Delete one app unsubscribe from one email list or remove one object from your space. One only. | Deciding what to stop is as powerful as deciding what to start — and usually harder to do honestly. | What would be different if you stopped doing that one thing for just one week? | Tomorrow is about the people in your life — and what this month may have quietly shifted there.
26 | Day 26: Your People | Notice which relationships give you energy and which ones quietly drain it — without judgment. | Write the names of 3 people who make you feel most like yourself. First ones that come to mind. | Write the name of one relationship you've been neglecting that matters. Send one message today. | Write one way you want to show up differently in your relationships over the next 30 days. | Reply to one message you've been putting off. One sentence is enough to show you're there. | Social connection is a stronger driver of wellbeing than most habits — including most in this workbook. | Which relationship would benefit most from you bringing more of what you've built this month? | Tomorrow you'll describe who you're becoming — in honest grounded terms not aspirational ones.
27 | Day 27: Who You're Becoming | Put words to the version of yourself you've been moving toward this month. | Write 5 words that describe the person you've been trying to be over the last 27 days. | Write 5 words that describe the person you were when you started on Day 1. | Look at both lists. Write one sentence about what's genuinely different — even if the shift is subtle. | Pick one word from your Day 27 list that feels most true right now. Write it somewhere visible. | Identity-level thinking — "I am someone who ___" — is more durable for lasting change than goal-setting. | If the person you were on Day 1 could see you right now what do you think they'd notice first? | Tomorrow you'll make one real commitment for after this workbook ends.
28 | Day 28: Your One Commitment | Choose one thing to keep doing after Day 30 — specific enough to actually follow through on. | Review what you've tried this month. What one habit or practice made the most real difference? | Write your commitment: "After Day 30 I will [specific behavior] at [specific time] on [specific days]." | Tell one person or write it somewhere permanent. A commitment only in your head is easier to drop. | Set a repeating phone reminder for your commitment. Label it with the reason it matters to you. | Specificity — naming the when where and how — is the strongest predictor of whether an intention holds. | What would make it easy to keep this commitment? What would make it hard? | Tomorrow you'll sketch a simple plan for staying in motion after Day 30 ends.
29 | Day 29: Life After Day 30 | Build a simple low-pressure plan to stay in forward motion when the workbook structure is gone. | Write your weekly rhythm for next month: which habits stay at what frequency and one check-in practice. | Decide what you'll do when things get hard again. Write your own re-entry plan in one or two sentences. | Choose one resource practice or person to lean on over the next 30 days. Write it down clearly. | Block 10 minutes in your calendar 30 days from today. Label it: "Month 2 check-in." | A pre-decided re-entry plan removes decision load when you're tired — making it far easier to return. | What does "staying in motion" look like for you on a real average week — not a perfect one? | Day 30 tomorrow. The last page. You'll close this the right way.
30 | Day 30: You Did It | Close this chapter with honesty acknowledgment and a clear view of what you've actually built. | Write 1–2 sentences to your Day 1 self. What's the one thing you'd most want them to know right now? | Read your Setup Pages your Life Audit and your original intention. Write one thing that surprised you. | Choose your next step — one more focused month a longer practice or simply protecting what you've built. | Put this workbook somewhere visible. Not a shelf. Somewhere it can remind you what you're capable of. | A deliberate closing ritual creates a clear ending — making it easier to begin the next chapter with intention. | What do you know about yourself now that you didn't know on Day 1? | There's no Day 31. You carry this forward — at your pace on your terms one small step at a time.
```

---

## SECTION 5 — COMPLETE PAGE ORDER REFERENCE

Generate pages in this exact order:

```
01  Front Cover
02  Welcome
03  Why You Feel Stuck
04  How to Use This Workbook
05  Quick Start
06  Life Audit
07  90-Day Picture & 30-Day Focus
08  Personal Reset Rules
09  Week 1 Overview (Days 1–7)
10  Day 1
11  Day 2
12  Day 3
13  Day 4
14  Day 5
15  Day 6
16  Day 7
17  Week 1 Checkpoint
18  Week 2 Overview (Days 8–14)
19  Day 8
20  Day 9
21  Day 10
22  Day 11
23  Day 12
24  Day 13
25  Day 14
26  Week 2 Checkpoint
27  Week 3 Overview (Days 15–21)
28  Day 15
29  Day 16
30  Day 17
31  Day 18
32  Day 19
33  Day 20
34  Day 21
35  Week 3 Checkpoint
36  Week 4 Overview (Days 22–30)
37  Day 22
38  Day 23
39  Day 24
40  Day 25
41  Day 26
42  Day 27
43  Day 28
44  Day 29
45  Day 30
46  Final Checkpoint (Day 30)
47  30-Day Habit Tracker Grid
48  30-Day Mood Log
49  Weekly Review Template
50  Health & Body Tracker
51  Focus & Productivity Tracker
52  Home & Environment Tracker
53  Money & Finances Tracker
54  Relationships & Connection Tracker
55  50 Tiny Habits
56  7-Day Emergency Reset
57  90-Day Continuation Roadmap
```

---

## SECTION 6 — QUALITY RULES (enforce in every line of code)

1. **Text wrapping is mandatory.** Use ReportLab's `Paragraph` with `ParagraphStyle` for all body text, or implement manual word-wrap using `c.stringWidth()`. Text must NEVER overflow its bounding box.

2. **Every page has a background.** The very first drawing call on every page is the full-page `COLOR_BG` rectangle.

3. **No banned words** anywhere in the output: transform, journey, unlock, level up, optimize, hack, dominate, crush, supercharge.

4. **Consistent spacing.** Define a vertical position tracker `y` that decrements as elements are drawn, ensuring nothing overlaps.

5. **Safe margin respected.** No text or element should appear within 36pt of any page edge.

6. **All 30 daily pages use the same function.** Write one function `draw_daily_page(c, day_data)` and call it in a loop. No copy-paste per-day code.

7. **Emoji support.** For the mood row (`😊 / 😐 / 😔`), use a Unicode-compatible font registration. If emoji rendering fails silently, fall back to text: `:) / :| / :(`

8. **Font fallback.** Wrap all font registration in try/except. If a custom font fails, fall back to Helvetica/Helvetica-Bold/Times-Italic.

9. **The script must print progress** to stdout as it runs, e.g.: `print("Drawing page 10: Day 1...")` — so the user can see it working.

10. **Final line** of the script: `print("Done! Saved to 30_Day_Life_Reset_Workbook.pdf")`

---

## SECTION 7 — OUTPUT EXPECTATIONS

Your response must be a single Python script (one code block). It must:

- Start with all imports and constants
- Define all helper functions (background, rounded_rect, sage_rule, writing_lines, draw_leaf, get_font, draw_daily_page)
- Include all content as Python strings/dicts inside the script — no external file reads required
- Generate all 57 pages in order
- Save the PDF to `30_Day_Life_Reset_Workbook.pdf`
- Run successfully with: `pip install reportlab && python generate_workbook.py`

Begin writing the script now. Start with the imports.

## ═══════════════════════════════════════════════════════
## END OF PROMPT
## ═══════════════════════════════════════════════════════
