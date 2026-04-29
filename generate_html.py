import os
import csv
import re
import markdown

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>30-Day Life Reset Workbook</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
    :root {
        --bg: #FAF8F6;
        --sage: #848B6F;
        --warm: #EFE8DF;
        --text: #333333;
    }
    body {
        margin: 0;
        padding: 0;
        background-color: #eee;
        font-family: 'Inter', sans-serif;
        color: var(--text);
    }
    @page {
        size: letter;
        margin: 0.5in;
    }
    .page {
        background-color: var(--bg);
        width: 8.5in;
        height: 11in;
        box-sizing: border-box;
        padding: 0.5in;
        margin: 0 auto 20px auto;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        page-break-after: always;
        overflow: hidden;
        position: relative;
    }
    @media print {
        body { background-color: var(--bg); }
        .page {
            margin: 0;
            box-shadow: none;
            width: 100%;
            height: 100%;
            page-break-after: always;
        }
    }
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Montserrat', sans-serif;
        color: var(--text);
        font-weight: 600;
        margin-top: 0;
    }
    h2 {
        color: var(--sage);
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 24px;
        border-bottom: 1px solid var(--sage);
        padding-bottom: 10px;
    }
    h3 {
        font-size: 20px;
    }
    p, li, td, th {
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        line-height: 1.6;
        color: var(--text);
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
    }
    th, td {
        border: 1px solid var(--sage);
        padding: 10px;
        text-align: left;
    }
    th {
        background-color: var(--warm);
        font-weight: 600;
    }
    blockquote {
        background-color: var(--warm);
        border-left: 4px solid var(--sage);
        margin: 20px 0;
        padding: 15px 20px;
        font-style: italic;
    }
    .daily-page {
        display: flex;
        flex-direction: column;
        height: 100%;
    }
    .top-zone {
        height: 18%;
    }
    .middle-zone {
        height: 57%;
    }
    .bottom-zone {
        height: 25%;
        border-top: 2px solid var(--warm);
        padding-top: 15px;
    }
    .daily-day-number {
        font-family: 'Montserrat', sans-serif;
        color: var(--sage);
        font-size: 14px;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    .daily-title {
        font-family: 'Montserrat', sans-serif;
        font-size: 26px;
        font-weight: 600;
        margin: 5px 0 10px 0;
    }
    .daily-goal {
        font-style: italic;
        color: #555;
        font-size: 15px;
    }
    .section-title {
        font-family: 'Montserrat', sans-serif;
        color: var(--sage);
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 10px;
    }
    .task-list {
        list-style-type: decimal;
        margin-left: 20px;
        margin-bottom: 20px;
    }
    .task-list li {
        margin-bottom: 15px;
        font-size: 15px;
    }
    .quick-win {
        background-color: var(--warm);
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    .why-it-works {
        font-size: 13px;
        color: #666;
    }
    .reflection-box {
        margin-bottom: 15px;
        flex-grow: 1;
    }
    .mood-scale {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
    }
    .mood-emojis {
        font-size: 20px;
        letter-spacing: 10px;
    }
    .tomorrow-focus {
        font-size: 13px;
        color: #777;
        font-style: italic;
    }
</style>
</head>
<body>
"""

def generate_html():
    with open(r'c:\Users\PC\Documents\Claude\Projects\30-Day Life Reset Workbook\30-day-life-reset\content\all_chunks_combined.md', 'r', encoding='utf-8') as f:
        md_text = f.read()
        
    sections = re.split(r'\n---\n', md_text)
    html_content = html_template
    
    csv_path = r"c:\Users\PC\Documents\Claude\Projects\30-Day Life Reset Workbook\30-day-life-reset\csv\daily_pages.csv"
    daily_data = {}
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            daily_data[row['Day_Number']] = row
            
    for sec in sections:
        sec = sec.strip()
        if not sec:
            continue
            
        # Clean metadata
        sec = re.sub(r'^# CHUNK.*\n?', '', sec, flags=re.MULTILINE)
        sec = re.sub(r'^## Status: DRAFT.*\n?', '', sec, flags=re.MULTILINE)
        sec = re.sub(r'^## Generated: .*\n?', '', sec, flags=re.MULTILINE)
        sec = re.sub(r'^## End Chunk.*\n?', '', sec, flags=re.MULTILINE)
        sec = sec.strip()
        
        if not sec:
            continue
            
        if re.search(r'^### Day (\d+):', sec, re.MULTILINE):
            match = re.search(r'^### Day (\d+):', sec, re.MULTILINE)
            if match:
                day_num = match.group(1)
                data = daily_data.get(day_num)
                if data:
                    html_content += f'''
<div class="page">
    <div class="daily-page">
        <div class="top-zone">
            <div class="daily-day-number">DAY {day_num}</div>
            <div class="daily-title">{data['Title']}</div>
            <div class="daily-goal">Goal: {data['Goal']}</div>
        </div>
        <div class="middle-zone">
            <div class="section-title">TASKS</div>
            <ol class="task-list">
                <li>{data['Task_1']}</li>
                <li>{data['Task_2']}</li>
                <li>{data['Task_3']}</li>
            </ol>
            <div class="quick-win">
                <div class="section-title">QUICK WIN</div>
                {data['Quick_Win']}
            </div>
            <div class="why-it-works">
                <span style="font-weight: 600; color: var(--sage);">WHY IT WORKS:</span> {data['Why_It_Works']}
            </div>
        </div>
        <div class="bottom-zone">
            <div class="reflection-box">
                <div class="section-title">REFLECTION</div>
                <p>{data['Reflection']}</p>
            </div>
            <div class="mood-scale">
                <div class="section-title" style="margin-bottom:0;">MOOD CHECK</div>
                <div class="mood-emojis">{data.get('Mood_Scale', '😊 / 😐 / 😔')}</div>
            </div>
            <div class="tomorrow-focus">
                Tomorrow: {data['Tomorrow_Focus']}
            </div>
        </div>
    </div>
</div>
'''
            continue
            
        html_sec = markdown.markdown(sec, extensions=['tables'])
        html_sec = html_sec.replace('<hr />', '<hr style="border: 0; border-top: 1px solid var(--sage); margin: 20px 0;">')
        html_sec = re.sub(r'(_{10,})', '<div style="border-bottom: 1px dotted var(--sage); margin: 15px 0; height: 20px;"></div>', html_sec)
        html_content += f'<div class="page">\n{html_sec}\n</div>\n'
        
    html_content += "</body>\n</html>"
    
    with open(r'c:\Users\PC\Documents\Claude\Projects\30-Day Life Reset Workbook\workbook.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

if __name__ == '__main__':
    generate_html()
