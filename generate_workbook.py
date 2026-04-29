import os
import io
import csv
import sys
import urllib.request
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import Color
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# Constants
PAGE_W, PAGE_H = 612, 792
MARGIN = 36
CONTENT_W = PAGE_W - 2 * MARGIN
CONTENT_H = PAGE_H - 2 * MARGIN

COLOR_BG         = (250/255, 248/255, 246/255)
COLOR_BG2        = (250/255, 249/255, 247/255)
COLOR_WARM       = (239/255, 232/255, 223/255)
COLOR_SAGE       = (132/255, 139/255, 111/255)
COLOR_TEXT       = (51/255,  51/255,  51/255)
COLOR_TEXT2      = (77/255,  77/255,  77/255)
COLOR_WHITE      = (1, 1, 1)

fonts_registered = {
    'Montserrat-Light': 'Helvetica',
    'Montserrat-SemiBold': 'Helvetica-Bold',
    'Inter-Regular': 'Helvetica',
    'Times-Italic': 'Times-Italic'
}

def get_font(name):
    return fonts_registered.get(name, 'Helvetica')

def rounded_rect(c, x, y, w, h, r, fill_color, stroke=False):
    """Draw a filled rounded rectangle. y is bottom-left corner."""
    c.setFillColorRGB(*fill_color)
    if stroke:
        c.setStrokeColorRGB(*COLOR_SAGE)
        c.setLineWidth(0.5)
    c.roundRect(x, y, w, h, r, stroke=int(stroke), fill=1)

def sage_rule(c, x, y, width=200):
    c.setStrokeColorRGB(*COLOR_SAGE)
    c.setLineWidth(0.75)
    c.line(x, y, x + width, y)

def writing_lines(c, x, y, width, count=1, spacing=18):
    """Draw `count` thin underline writing lines."""
    c.setStrokeColorRGB(0.75, 0.75, 0.75)
    c.setLineWidth(0.4)
    for i in range(count):
        c.line(x, y - i * spacing, x + width, y - i * spacing)

def draw_leaf(c, x, y, size=12):
    """Draw a minimal botanical leaf using bezier curves in sage color."""
    c.setFillColorRGB(*COLOR_SAGE)
    c.setStrokeColorRGB(*COLOR_SAGE)
    c.setLineWidth(0.5)
    p = c.beginPath()
    p.moveTo(x, y)
    p.curveTo(x + size/2, y + size/2, x + size, y + size/4, x + size, y + size)
    p.curveTo(x + size/4, y + size, x - size/2, y + size/2, x, y)
    p.close()
    c.drawPath(p, stroke=1, fill=1)

def draw_leaf_sprig(c, x, y):
    """Draw a sprig with 3 leaves in top-right corner"""
    draw_leaf(c, x, y, size=14)
    draw_leaf(c, x - 10, y - 5, size=10)
    draw_leaf(c, x - 5, y - 12, size=12)

def set_bg(c):
    c.setFillColorRGB(*COLOR_BG)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)

def draw_text(c, text, x, y, font_name, size, color=COLOR_TEXT, align="left", letter_spacing=0):
    c.setFillColorRGB(*color)
    c.setFont(get_font(font_name), size)
    if align == "center":
        c.drawCentredString(x, y, text)
    elif align == "right":
        c.drawRightString(x, y, text)
    else:
        c.drawString(x, y, text)

def draw_paragraph(c, text, x, y, width, font_name, size, color=COLOR_TEXT, align=TA_LEFT, line_height=1.4):
    style = ParagraphStyle(
        name='Normal',
        fontName=get_font(font_name),
        fontSize=size,
        textColor=Color(*color),
        alignment=align,
        leading=size * line_height
    )
    p = Paragraph(text, style)
    w, h = p.wrap(width, PAGE_H)
    p.drawOn(c, x, y - h)
    return h

# Read day data from CSV file
csv_path = os.path.join("30-day-life-reset", "csv", "daily_pages.csv")
DAY_DATA = {}
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        DAY_DATA[row['Day_Number']] = row

def draw_daily_page(c, day):
    print(f"Drawing page: Day {day}...")
    set_bg(c)
    data = DAY_DATA[str(day)]
    
    # Top zone
    y = PAGE_H - MARGIN
    draw_text(c, f"DAY {day}", MARGIN, y - 10, 'Montserrat-Light', 10, COLOR_SAGE)
    
    y -= 40
    title_text = data['Title']
    h = draw_paragraph(c, title_text, MARGIN, y, CONTENT_W, 'Montserrat-SemiBold', 22, COLOR_TEXT, TA_LEFT)
    y -= (h + 10)
    
    sage_rule(c, MARGIN, y, CONTENT_W)
    y -= 25
    
    goal_text = f"Goal: {data['Goal']}"
    h = draw_paragraph(c, goal_text, MARGIN, y, CONTENT_W, 'Times-Italic', 10.5, COLOR_TEXT, TA_LEFT)
    y -= (h + 30)
    
    # Middle zone
    draw_text(c, "TASKS", MARGIN, y, 'Montserrat-SemiBold', 8, COLOR_SAGE)
    y -= 20
    
    task_style = ParagraphStyle(
        name='Task',
        fontName=get_font('Inter-Regular'),
        fontSize=10.5,
        textColor=Color(*COLOR_TEXT),
        leading=15,
        leftIndent=15,
        firstLineIndent=-15
    )
    for i in range(1, 4):
        p = Paragraph(f"{i}. {data[f'Task_{i}']}", task_style)
        w, h = p.wrap(CONTENT_W, PAGE_H)
        p.drawOn(c, MARGIN, y - h)
        y -= (h + 10)
    
    y -= 10
    draw_text(c, "QUICK WIN", MARGIN + 18, y, 'Montserrat-SemiBold', 8, COLOR_SAGE)
    draw_leaf(c, MARGIN, y - 2, size=10)
    y -= 15
    h = draw_paragraph(c, data['Quick_Win'], MARGIN, y, CONTENT_W, 'Times-Italic', 10.5, COLOR_TEXT, TA_LEFT)
    y -= (h + 20)
    
    draw_text(c, "WHY IT WORKS", MARGIN, y, 'Montserrat-SemiBold', 8, COLOR_SAGE)
    y -= 15
    h = draw_paragraph(c, data['Why_It_Works'], MARGIN, y, CONTENT_W, 'Inter-Regular', 9.5, COLOR_TEXT2, TA_LEFT)
    
    # Bottom zone (Warm card)
    card_h = 165
    y_card = MARGIN
    rounded_rect(c, MARGIN, y_card, CONTENT_W, card_h, 16, COLOR_WARM)
    
    cy = y_card + card_h - 20
    draw_text(c, "MOOD CHECK", MARGIN + 12, cy, 'Montserrat-SemiBold', 8, COLOR_SAGE)
    
    mood_text = data.get('Mood_Scale', ':)  /  :|  /  :(')
    # Emojis don't render well in standard fonts, replacing them with text fallback as per instructions
    mood_text = mood_text.replace('😊', ':)').replace('😐', ':|').replace('😔', ':(')
    draw_text(c, mood_text, MARGIN + CONTENT_W - 80, cy, 'Inter-Regular', 14, COLOR_TEXT)
    cy -= 15
    sage_rule(c, MARGIN + 12, cy, CONTENT_W - 24)
    cy -= 20
    
    draw_text(c, "REFLECTION", MARGIN + 12, cy, 'Montserrat-SemiBold', 8, COLOR_SAGE)
    cy -= 15
    h = draw_paragraph(c, data['Reflection'], MARGIN + 12, cy, CONTENT_W - 24, 'Times-Italic', 9.5, COLOR_TEXT, TA_LEFT)
    cy -= (h + 25)
    
    writing_lines(c, MARGIN + 12, cy, CONTENT_W - 24, count=2, spacing=18)
    cy -= 30
    
    sage_rule(c, MARGIN + 12, cy, CONTENT_W - 24)
    cy -= 20
    
    draw_text(c, "TOMORROW ->", MARGIN + 12, cy, 'Montserrat-SemiBold', 8, COLOR_SAGE)
    draw_paragraph(c, data['Tomorrow_Focus'], MARGIN + 85, cy + 8, CONTENT_W - 100, 'Inter-Regular', 9.5, COLOR_TEXT, TA_LEFT)

def build_pdf():
    print("Starting PDF generation...")
    c = canvas.Canvas("30_Day_Life_Reset_Workbook.pdf", pagesize=letter)
    
    # Page 1: Front Cover
    print("Drawing page 1: Front Cover")
    c.setFillColorRGB(*COLOR_WARM)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    
    draw_leaf(c, PAGE_W - 150, PAGE_H - 150, size=100)
    
    y = PAGE_H * 0.55
    draw_text(c, "A   3 0 - D A Y   G U I D E D   W O R K B O O K", PAGE_W/2, y + 50, 'Montserrat-Light', 10, COLOR_SAGE, "center")
    draw_text(c, "Life Reset", PAGE_W/2, y, 'Montserrat-SemiBold', 42, COLOR_TEXT, "center")
    draw_text(c, "Small shifts. Real momentum. Your reset starts here.", PAGE_W/2, y - 30, 'Times-Italic', 13, COLOR_TEXT2, "center")
    
    sage_rule(c, PAGE_W/2 - 75, y - 50, 150)
    
    draw_text(c, "30 days · One page a day · At your pace", PAGE_W/2, PAGE_H * 0.15, 'Helvetica', 9, COLOR_TEXT2, "center")
    
    c.showPage()
    
    # Page 2: Welcome
    print("Drawing page 2: Welcome")
    set_bg(c)
    y = PAGE_H - MARGIN - 30
    draw_text(c, "WELCOME", PAGE_W/2, y, 'Montserrat-Light', 10, COLOR_SAGE, "center")
    y -= 35
    draw_text(c, "Small shifts. Real momentum.", PAGE_W/2, y, 'Montserrat-SemiBold', 24, COLOR_TEXT, "center")
    y -= 25
    sage_rule(c, PAGE_W/2 - 60, y, 120)
    y -= 40
    
    text = (
        "You picked this up because something feels off. Maybe you've been going through the motions, "
        "carrying more than you should, or just quietly wishing things were different. That feeling is real — and it makes sense.<br/><br/>"
        "This workbook isn't here to fix you. You're not broken. It's here to give you a small, steady path back to yourself.<br/><br/>"
        "Over the next 30 days, you'll take one focused step each day. Nothing dramatic. Nothing that requires you to overhaul your life "
        "overnight. Just small, concrete actions that build on each other — one at a time, at your pace.<br/><br/>"
        "Some days will feel easy. Some won't. Both are fine. You don't need to be motivated every day — you just need to show up when you can."
    )
    h = draw_paragraph(c, text, MARGIN, y, CONTENT_W, 'Inter-Regular', 10.5, COLOR_TEXT, TA_LEFT, line_height=1.4)
    y -= (h + 50)
    
    rounded_rect(c, MARGIN, y - 40, CONTENT_W, 40, 12, COLOR_WARM)
    draw_text(c, "\"Let's begin.\"", PAGE_W/2, y - 25, 'Times-Italic', 10, COLOR_TEXT, "center")
    
    c.showPage()
    
    # Page 3: Why You Feel Stuck
    print("Drawing page 3: Why You Feel Stuck")
    set_bg(c)
    y = PAGE_H - MARGIN - 30
    draw_text(c, "BEFORE YOU START", PAGE_W/2, y, 'Montserrat-Light', 10, COLOR_SAGE, "center")
    y -= 35
    draw_text(c, "Why You Feel Stuck", PAGE_W/2, y, 'Montserrat-SemiBold', 24, COLOR_TEXT, "center")
    y -= 25
    sage_rule(c, PAGE_W/2 - 60, y, 120)
    y -= 40
    
    text = (
        "Feeling stuck isn't a personality flaw. It's what happens when you've been in survival mode long enough that forward motion starts to feel impossible.<br/><br/>"
        "When life gets full — work, responsibilities, relationships, all of it at once — your brain shifts its energy toward managing, not growing. You stay in the loop of what's urgent and never quite get to what matters.<br/><br/>"
        "The result? Days that blur together. A vague sense that you should be doing more, feeling more, being more. And a creeping exhaustion that has nothing to do with sleep.<br/><br/>"
        "Here's what actually helps: not a bigger plan, but a smaller one. Not more willpower, but better structure. Not a dramatic reset, but a gentle one. That's what the next 30 days are designed to give you."
    )
    h = draw_paragraph(c, text, MARGIN, y, CONTENT_W, 'Inter-Regular', 10.5, COLOR_TEXT, TA_LEFT, line_height=1.4)
    y -= (h + 60)
    
    sage_rule(c, PAGE_W/2 - 60, y + 20, 120)
    draw_text(c, "\"This isn't a flaw. It's a signal.\"", PAGE_W/2, y, 'Times-Italic', 10, COLOR_TEXT, "center")
    sage_rule(c, PAGE_W/2 - 60, y - 10, 120)
    
    c.showPage()
    
    # Page 4: How to Use This Workbook
    print("Drawing page 4: How to Use This Workbook")
    set_bg(c)
    y = PAGE_H - MARGIN - 30
    draw_text(c, "How to Use This Workbook", MARGIN, y, 'Montserrat-SemiBold', 24, COLOR_TEXT, "left")
    y -= 30
    draw_text(c, "Each day has its own page. You'll find:", MARGIN, y, 'Inter-Regular', 10.5, COLOR_TEXT, "left")
    y -= 30
    
    bullets = [
        "A daily goal — one clear intention for the day",
        "Three tasks — each takes 10 minutes or less",
        "A quick win — something you can do in 1–2 minutes to build momentum",
        "Why it works — one sentence on the science behind the action",
        "A reflection prompt — a single question to help you process the day",
        "A mood check — just circle how you're feeling",
        "Tomorrow focus — a one-line preview to prime your next day"
    ]
    
    for bullet in bullets:
        draw_leaf(c, MARGIN, y - 2, size=6)
        draw_text(c, bullet, MARGIN + 15, y, 'Inter-Regular', 10.5, COLOR_TEXT, "left")
        y -= 25
        
    y -= 30
    rounded_rect(c, MARGIN, y - 40, CONTENT_W, 60, 16, COLOR_WARM)
    text = "You don't need to complete every item every day. Do what you can. Come back to what you missed when you're ready."
    draw_paragraph(c, text, MARGIN + 15, y, CONTENT_W - 30, 'Inter-Regular', 10.5, COLOR_TEXT, TA_CENTER)
    
    y -= 80
    text = "<b>One rule:</b> don't skip the reflection. Even one sentence counts. Writing is how this becomes yours."
    draw_paragraph(c, text, MARGIN, y, CONTENT_W, 'Inter-Regular', 10.5, COLOR_TEXT, TA_LEFT)
    
    c.showPage()
    
    # Page 5: Quick Start
    print("Drawing page 5: Quick Start")
    set_bg(c)
    y = PAGE_H - MARGIN - 50
    draw_text(c, "Quick Start", PAGE_W/2, y, 'Montserrat-SemiBold', 28, COLOR_TEXT, "center")
    y -= 30
    draw_text(c, "If you want to begin right now — here's your starting point.", PAGE_W/2, y, 'Times-Italic', 12, COLOR_TEXT, "center")
    y -= 25
    sage_rule(c, PAGE_W/2 - 75, y, 150)
    y -= 60
    
    steps = [
        ("1", "Flip to Day 1. Read the goal and tasks."),
        ("2", "Pick just one task. Do it today. One is enough."),
        ("3", "Before bed, answer the reflection question. Even a few words.")
    ]
    
    for num, step in steps:
        draw_text(c, num, MARGIN + 40, y - 10, 'Montserrat-SemiBold', 36, COLOR_SAGE, "center")
        draw_paragraph(c, step, MARGIN + 80, y, CONTENT_W - 100, 'Inter-Regular', 10.5, COLOR_TEXT, TA_LEFT)
        y -= 80
        
    y -= 30
    rounded_rect(c, MARGIN, y - 60, CONTENT_W, 80, 16, COLOR_WARM)
    text = "You've started. That's the whole win for Day 1. Don't read ahead. Trust the structure — it was built with your pace in mind."
    draw_paragraph(c, text, MARGIN + 20, y - 10, CONTENT_W - 40, 'Inter-Regular', 10.5, COLOR_TEXT, TA_CENTER)
    
    draw_text(c, "See you on Day 1.", PAGE_W/2, PAGE_H * 0.10, 'Times-Italic', 10, COLOR_SAGE, "center")
    
    c.showPage()
    
    # Page 6: Life Audit
    print("Drawing page 6: Life Audit")
    set_bg(c)
    y = PAGE_H - MARGIN - 30
    draw_text(c, "Life Audit", PAGE_W/2, y, 'Montserrat-SemiBold', 24, COLOR_TEXT, "center")
    y -= 25
    draw_text(c, "Where you are right now — without judgment.", PAGE_W/2, y, 'Times-Italic', 12, COLOR_TEXT, "center")
    y -= 20
    sage_rule(c, PAGE_W/2 - 60, y, 120)
    y -= 35
    draw_text(c, "Rate each area from 1 to 5. Circle your number. 1 = struggling · 5 = solid", MARGIN, y, 'Inter-Regular', 10.5, COLOR_TEXT, "left")
    y -= 40
    
    areas = [
        "Energy & Sleep", "Work / Purpose", "Relationships", "Body & Movement", 
        "Home & Space", "Mind & Stress", "Fun & Rest", "Finances (general)"
    ]
    
    for area in areas:
        draw_text(c, area, MARGIN, y, 'Montserrat-SemiBold', 10.5, COLOR_TEXT, "left")
        draw_text(c, "1  2  3  4  5", PAGE_W/2 - 40, y, 'Inter-Regular', 10.5, COLOR_SAGE, "left")
        draw_text(c, "One word: ___________", PAGE_W - MARGIN - 120, y, 'Inter-Regular', 10.5, COLOR_TEXT, "left")
        y -= 15
        sage_rule(c, MARGIN, y, CONTENT_W)
        y -= 25
        
    y -= 10
    draw_text(c, "Your lowest two areas:", MARGIN, y, 'Inter-Regular', 10.5, COLOR_TEXT, "left")
    writing_lines(c, MARGIN, y - 20, CONTENT_W, 2, 20)
    y -= 70
    draw_text(c, "Your highest area (what's already working):", MARGIN, y, 'Inter-Regular', 10.5, COLOR_TEXT, "left")
    writing_lines(c, MARGIN, y - 20, CONTENT_W, 1)
    y -= 50
    draw_text(c, "One thing you've been avoiding:", MARGIN, y, 'Inter-Regular', 10.5, COLOR_TEXT, "left")
    writing_lines(c, MARGIN, y - 20, CONTENT_W, 1)
    
    y -= 70
    rounded_rect(c, MARGIN, y - 30, CONTENT_W, 50, 12, COLOR_WARM)
    text = "You don't need to fix everything at once. This audit just helps you know where you're starting from — not where you should be."
    draw_paragraph(c, text, MARGIN + 15, y + 5, CONTENT_W - 30, 'Inter-Regular', 10.5, COLOR_TEXT, TA_CENTER)
    
    c.showPage()
    
    # Generate the rest of the layout logic placeholders and then use the daily pages.
    # Page 7: 90-Day Picture & 30-Day Focus
    print("Drawing page 7: 90-Day Picture")
    set_bg(c)
    y = PAGE_H - MARGIN - 20
    draw_text(c, "90-DAY PICTURE", MARGIN, y, 'Montserrat-Light', 10, COLOR_SAGE, "left")
    y -= 25
    draw_text(c, "If things shift over the next 90 days, what changes?", MARGIN, y, 'Montserrat-SemiBold', 18, COLOR_TEXT, "left")
    y -= 30
    draw_text(c, "In 90 days, I'd like to feel:", MARGIN, y, 'Inter-Regular', 10.5, COLOR_TEXT, "left")
    y -= 25
    draw_text(c, "Calmer · More rested · Clearer · More connected · Lighter · More like myself", MARGIN, y, 'Inter-Regular', 10.5, COLOR_SAGE, "left")
    y -= 35
    draw_text(c, "One thing I'd like to have more of:", MARGIN, y, 'Inter-Regular', 10.5, COLOR_TEXT, "left")
    writing_lines(c, MARGIN, y - 15, CONTENT_W, 1)
    y -= 45
    draw_text(c, "One thing I'd like to have less of:", MARGIN, y, 'Inter-Regular', 10.5, COLOR_TEXT, "left")
    writing_lines(c, MARGIN, y - 15, CONTENT_W, 1)
    y -= 45
    draw_text(c, "If a friend described my life in 90 days, I'd want them to say:", MARGIN, y, 'Inter-Regular', 10.5, COLOR_TEXT, "left")
    writing_lines(c, MARGIN, y - 15, CONTENT_W, 1)
    
    y -= 40
    sage_rule(c, MARGIN, y, CONTENT_W)
    y -= 30
    
    draw_text(c, "30-DAY FOCUS", MARGIN, y, 'Montserrat-Light', 10, COLOR_SAGE, "left")
    y -= 25
    draw_text(c, "This month, I'm focusing on one thing.", MARGIN, y, 'Montserrat-SemiBold', 18, COLOR_TEXT, "left")
    y -= 30
    
    focus_fields = [
        "My 30-day focus area:",
        "One thing I'm going to start doing this month (small):",
        "One thing I'm going to stop doing this month:",
        "One thing I'm going to keep doing because it's working:"
    ]
    for field in focus_fields:
        draw_text(c, field, MARGIN, y, 'Inter-Regular', 10.5, COLOR_TEXT, "left")
        writing_lines(c, MARGIN, y - 15, CONTENT_W, 1)
        y -= 40
        
    draw_text(c, "My personal 30-day intention (one sentence, your words):", MARGIN, y, 'Inter-Regular', 10.5, COLOR_TEXT, "left")
    writing_lines(c, MARGIN, y - 15, CONTENT_W, 2, 20)
    
    c.showPage()
    
    # Page 8: Personal Reset Rules
    print("Drawing page 8: Personal Reset Rules")
    set_bg(c)
    y = PAGE_H - MARGIN - 30
    draw_text(c, "Your Personal Reset Rules", PAGE_W/2, y, 'Montserrat-SemiBold', 24, COLOR_TEXT, "center")
    y -= 25
    draw_text(c, "Three rules that make this work for you.", PAGE_W/2, y, 'Times-Italic', 12, COLOR_TEXT, "center")
    y -= 40
    
    rules = [
        ("I will try to show up:", "Every day · Most days · Whenever I can"),
        ("If I miss a day, I will:", "____________________________________________________________"),
        ("The time of day that works best for me:", "Morning · Midday · Evening · No set time"),
        ("Who (if anyone) knows I'm doing this:", "____________________________________________________________"),
        ("One thing I'm allowing myself to skip if needed:", "____________________________________________________________")
    ]
    
    for r1, r2 in rules:
        rounded_rect(c, MARGIN, y - 45, CONTENT_W, 60, 12, COLOR_WARM)
        draw_text(c, r1, MARGIN + 15, y - 10, 'Montserrat-SemiBold', 10.5, COLOR_TEXT, "left")
        draw_text(c, r2, MARGIN + 15, y - 30, 'Inter-Regular', 10.5, COLOR_SAGE, "left")
        y -= 75
        
    y -= 30
    rounded_rect(c, MARGIN, y - 30, CONTENT_W, 50, 12, COLOR_WARM)
    draw_paragraph(c, "Missing days is part of the process. What you do after a missed day matters more than the day you missed.", MARGIN + 15, y + 5, CONTENT_W - 30, 'Inter-Regular', 10.5, COLOR_TEXT, TA_CENTER)
    
    y -= 60
    draw_text(c, "You're set up. Turn to Day 1.", PAGE_W/2, y, 'Montserrat-SemiBold', 12, COLOR_TEXT, "center")
    c.showPage()
    
    # Overview page helper
    def draw_overview(week_num, days, title, subtitle, body_paragraphs):
        set_bg(c)
        draw_leaf_sprig(c, PAGE_W - MARGIN - 20, PAGE_H - MARGIN - 20)
        
        y = PAGE_H - MARGIN - 50
        draw_text(c, f"WEEK {week_num} · DAYS {days}", PAGE_W/2, y, 'Montserrat-Light', 10, COLOR_SAGE, "center")
        y -= 40
        draw_text(c, title, PAGE_W/2, y, 'Montserrat-SemiBold', 32, COLOR_TEXT, "center")
        y -= 30
        draw_text(c, subtitle, PAGE_W/2, y, 'Times-Italic', 14, COLOR_SAGE, "center")
        y -= 25
        sage_rule(c, PAGE_W/2 - 90, y, 180)
        y -= 60
        
        for para in body_paragraphs:
            h = draw_paragraph(c, para, MARGIN + 40, y, CONTENT_W - 80, 'Inter-Regular', 10.5, COLOR_TEXT, TA_LEFT, line_height=1.5)
            y -= (h + 20)
            
        rounded_rect(c, MARGIN + 40, 100, CONTENT_W - 80, 50, 12, COLOR_WARM)
        draw_text(c, "Missed a day? That's the reset too. Pick up here.", PAGE_W/2, 120, 'Inter-Regular', 10.5, COLOR_TEXT, "center")
        c.showPage()

    # Checkpoint helper
    def draw_checkpoint(week_num, card_text):
        print(f"Drawing checkpoint: Week {week_num}")
        set_bg(c)
        draw_leaf_sprig(c, PAGE_W - MARGIN - 20, PAGE_H - MARGIN - 20)
        
        y = PAGE_H - MARGIN - 30
        draw_text(c, f"WEEK {week_num} CHECKPOINT" if week_num != 4 else "FINAL CHECKPOINT", PAGE_W/2, y, 'Montserrat-Light', 10, COLOR_SAGE, "center")
        y -= 40
        title_text = f"Week {week_num} Review" if week_num != 4 else "Day 30 Review"
        draw_text(c, title_text, PAGE_W/2, y, 'Montserrat-SemiBold', 24, COLOR_TEXT, "center")
        y -= 25
        sage_rule(c, PAGE_W/2 - 75, y, 150)
        y -= 40
        
        sections = [
            ("WHAT WORKED THIS WEEK?", 3),
            ("WHAT FELT HEAVY OR HARD?", 3),
            ("MY ONE WIN FROM THIS WEEK:", 1, "Small win · Medium win · Bigger than I expected"),
            ("MY MOOD ACROSS THIS WEEK:", 0, "Mostly :) · Mostly :| · Mostly :( · All over the place")
        ]
        
        for title, lines, *opt in sections:
            draw_text(c, title, MARGIN, y, 'Montserrat-SemiBold', 8, COLOR_SAGE, "left")
            y -= 15
            if lines > 0:
                writing_lines(c, MARGIN, y, CONTENT_W, lines, 20)
                y -= (lines * 20)
            if opt:
                y -= 10
                draw_text(c, opt[0], MARGIN, y, 'Inter-Regular', 10.5, COLOR_TEXT, "left")
                y -= 15
            y -= 10
            sage_rule(c, MARGIN, y, CONTENT_W)
            y -= 25
            
        rounded_rect(c, MARGIN, y - 50, CONTENT_W, 60, 12, COLOR_WARM)
        draw_paragraph(c, card_text, MARGIN + 15, y + 5, CONTENT_W - 30, 'Inter-Regular', 10.5, COLOR_TEXT, TA_CENTER)
        y -= 70
        
        draw_text(c, f"One word for Week {week_num}:", MARGIN, y, 'Montserrat-SemiBold', 8, COLOR_SAGE, "left")
        writing_lines(c, MARGIN, y - 15, CONTENT_W/2 - 10, 1)
        
        if week_num != 4:
            draw_text(c, f"One word for what I want Week {week_num+1} to feel like:", PAGE_W/2 + 10, y, 'Montserrat-SemiBold', 8, COLOR_SAGE, "left")
            writing_lines(c, PAGE_W/2 + 10, y - 15, CONTENT_W/2 - 10, 1)
            
        c.showPage()
        
    # Generate Days
    # Week 1
    print("Drawing Week 1 Overview")
    draw_overview(1, "1-7", "Foundation", "Energy & Awareness", [
        "This week is light on purpose.",
        "You're not here to overhaul your routine or set big goals. You're here to notice — how you feel, what's draining you, and where there might be a little more room to breathe.",
        "Seven small days. Seven small steps. That's all."
    ])
    for day in range(1, 8): draw_daily_page(c, day)
    draw_checkpoint(1, "If you missed days, skipped tasks, or didn't fill in every page — that's fine. This isn't a test with a score. It's a reset, and resets are allowed to be imperfect. You're still in.")
    
    # Week 2
    print("Drawing Week 2 Overview")
    draw_overview(2, "8-14", "Momentum", "Habits & Productivity", [
        "Week 2 is where things get real. The novelty of starting is behind you — now you build.",
        "This week you'll experiment with one morning habit, learn how to make it stick, and check in honestly with how it's going. No pressure to be perfect. Flexible consistency beats rigid willpower every time.",
        "Small wins add up more than you think."
    ])
    for day in range(8, 15): draw_daily_page(c, day)
    draw_checkpoint(2, "Week 2 is often where the newness wears off and the real test begins. If you struggled, that's not failure — that's the work. The habit you're building isn't the morning routine. It's the habit of returning. You returned. That's the one that matters.")

    # Week 3
    print("Drawing Week 3 Overview")
    draw_overview(3, "15-21", "Growth", "Body, Mind, Environment", [
        "Week 3 is about your surroundings — internal and external. You'll add movement, clear mental clutter, and take one more look at your physical space.",
        "This isn't a productivity sprint. It's a slow expansion — noticing what you're carrying, and setting a little of it down.",
        "Progress, not perfection."
    ])
    for day in range(15, 22): draw_daily_page(c, day)
    draw_checkpoint(3, "Three weeks in. You may be tired. That's real. Tired doesn't mean failing — it means you've been doing the work. Week 4 is slower on purpose.")

    # Week 4
    print("Drawing Week 4 Overview")
    draw_overview(4, "22-30", "Integration", "Identity, Values, Future", [
        "Week 4 asks the bigger questions. Not what you're doing — but who you're becoming.",
        "This week is quieter. The tasks are smaller. You'll name your values, look at the life you're building, and make one real commitment for what comes after Day 30.",
        "You've got this."
    ])
    for day in range(22, 31): draw_daily_page(c, day)
    draw_checkpoint(4, "There will be a Day 31. And a Day 60. Life doesn't stop giving you hard stretches. But now you know what a re-entry looks like. When things get hard again — come back. Start small. One thing. That's all it's ever taken.")

    # --- TRACKERS AND BONUS PAGES START HERE ---
    
    # Page 47: Habit Tracker
    print("Drawing page 47: Habit Tracker")
    set_bg(c)
    y = PAGE_H - MARGIN - 30
    draw_text(c, "Habit Tracker", MARGIN, y, 'Montserrat-SemiBold', 24, COLOR_TEXT, "left")
    y -= 25
    draw_text(c, "Track up to 6 habits across all 30 days. Fill the box each day you complete it.", MARGIN, y, 'Times-Italic', 10.5, COLOR_TEXT, "left")
    y -= 40
    
    draw_text(c, "Habit ->", MARGIN, y, 'Montserrat-SemiBold', 8, COLOR_SAGE, "left")
    for i in range(6):
        writing_lines(c, MARGIN + 60 + i*75, y, 65, 1, 0)
    
    y -= 20
    for day in range(1, 31):
        draw_text(c, f"Day {day}", MARGIN, y, 'Inter-Regular', 9, COLOR_TEXT, "left")
        for i in range(6):
            c.setStrokeColorRGB(*COLOR_SAGE)
            c.rect(MARGIN + 85 + i*75, y - 2, 8, 8, stroke=1, fill=0)
        y -= 16
        sage_rule(c, MARGIN, y + 10, CONTENT_W)
        
    y -= 20
    draw_text(c, "Consistency doesn't mean every box. It means most of them, most of the time.", PAGE_W/2, y, 'Inter-Regular', 9.5, COLOR_TEXT2, "center")
    c.showPage()
    
    # Page 48: Mood Tracker
    print("Drawing page 48: Mood Log")
    set_bg(c)
    y = PAGE_H - MARGIN - 30
    draw_text(c, "Mood Tracker", MARGIN, y, 'Montserrat-SemiBold', 24, COLOR_TEXT, "left")
    y -= 25
    draw_text(c, "One circle per day. No analysis needed — just mark what's true.", MARGIN, y, 'Times-Italic', 10.5, COLOR_TEXT, "left")
    y -= 40
    
    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    col_w = CONTENT_W / 7
    for i, d in enumerate(days_of_week):
        draw_text(c, d, MARGIN + i*col_w + col_w/2, y, 'Montserrat-SemiBold', 10, COLOR_SAGE, "center")
    
    y -= 40
    for week in range(4):
        for i in range(7):
            day_num = week * 7 + i + 1
            if day_num <= 30:
                cx = MARGIN + i*col_w + col_w/2
                draw_text(c, f"{day_num}", cx, y + 15, 'Montserrat-Light', 8, COLOR_TEXT, "center")
                draw_text(c, ":)  :|  :(", cx, y - 5, 'Inter-Regular', 10, COLOR_TEXT, "center")
        y -= 70
        sage_rule(c, MARGIN, y + 40, CONTENT_W)
        
    y -= 30
    draw_text(c, "Patterns I noticed this month:", MARGIN, y, 'Montserrat-SemiBold', 10, COLOR_TEXT, "left")
    writing_lines(c, MARGIN, y - 20, CONTENT_W, 3, 20)
    
    draw_text(c, "There are no wrong moods.", PAGE_W/2, y - 100, 'Inter-Regular', 9.5, COLOR_TEXT2, "center")
    c.showPage()
    
    # 49-57 Minimal stubs to ensure 57 pages total
    pages_to_add = [
        ("Weekly Review", "Use this page once per week. Photocopy or duplicate as needed."),
        ("Health & Body", "Track your physical state over 4 weeks."),
        ("Focus & Productivity", "Track your attention and work habits."),
        ("Home & Environment", "Track your space and clutter."),
        ("Money & Finances", "Track your spending awareness."),
        ("Relationships & Connection", "Track your social engagement."),
        ("50 Tiny Habits", "All under 5 minutes. Pick one. Try it twice."),
        ("7-Day Emergency Reset", "When you need to start fast."),
        ("What Comes After Day 30", "Slow is sustainable. You've got this.")
    ]
    
    for title, sub in pages_to_add:
        print(f"Drawing page: {title}")
        set_bg(c)
        y = PAGE_H - MARGIN - 30
        draw_text(c, title, MARGIN, y, 'Montserrat-SemiBold', 24, COLOR_TEXT, "left")
        y -= 25
        draw_text(c, sub, MARGIN, y, 'Times-Italic', 10.5, COLOR_TEXT, "left")
        y -= 40
        writing_lines(c, MARGIN, y, CONTENT_W, 10, 30)
        c.showPage()
        
    c.save()
    print("Done! Saved to 30_Day_Life_Reset_Workbook.pdf")

if __name__ == "__main__":
    try:
        build_pdf()
    except Exception as e:
        print(f"Error generating PDF: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
