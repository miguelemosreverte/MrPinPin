#!/usr/bin/env python3
import json
import re
from pathlib import Path

def parse_markdown(md_file):
    """Parse the markdown file and extract story data"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title translations
    title_section = re.search(r'Title translations:(.*?)## Panel', content, re.DOTALL)
    titles = {}
    if title_section:
        for line in title_section.group(1).split('\n'):
            match = re.match(r'\s*-\s*(\w+):\s*(.+)', line)
            if match:
                titles[match.group(1)] = match.group(2).strip()
    
    # Extract panel descriptions
    panels = []
    panel_sections = re.findall(r'### Panel \d+ \(([^)]+)\)(.*?)(?=### Panel|\Z)', content, re.DOTALL)
    
    for filename, descriptions in panel_sections:
        panel_data = {'filename': filename}
        for line in descriptions.strip().split('\n'):
            match = re.match(r'-\s*(\w+):\s*(.+)', line)
            if match:
                lang = match.group(1)
                desc = match.group(2).strip()
                panel_data[lang] = desc
        panels.append(panel_data)
    
    return titles, panels

def generate_html(titles, panels, lang):
    """Generate HTML for a specific language"""
    
    html_template = """<!DOCTYPE html>
<html lang="{lang_code}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Kalam:wght@400;700&family=Comic+Neue:wght@400;700&display=swap');
        
        body {{
            font-family: 'Kalam', 'Comic Neue', 'Comic Sans MS', cursive;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
            line-height: 1.6;
        }}
        
        .page {{
            max-width: 1200px;
            margin: 0 auto 40px;
            background-color: white;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 40px;
            page-break-after: always;
        }}
        
        .page-header {{
            text-align: center;
            margin-bottom: 40px;
            font-size: 32px;
            color: #333;
            font-weight: 700;
            font-family: 'Comic Neue', 'Comic Sans MS', cursive;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }}
        
        .comic-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 25px;
            margin-bottom: 30px;
        }}
        
        .comic-panel {{
            background-color: #f9f9f9;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s ease;
            display: flex;
            flex-direction: column;
        }}
        
        .comic-panel:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
        }}
        
        .hero-panel {{
            grid-column: span 2;
            grid-row: span 2;
            display: flex;
            flex-direction: column;
        }}
        
        .hero-panel .panel-image {{
            width: 100%;
            height: auto;
            flex-grow: 1;
            object-fit: cover;
        }}
        
        .hero-panel .panel-caption {{
            font-size: 19px;
            padding: 20px;
            min-height: 80px;
            font-weight: 400;
        }}
        
        .panel-image {{
            width: 100%;
            height: auto;
            display: block;
        }}
        
        .panel-caption {{
            padding: 15px;
            font-size: 15px;
            text-align: center;
            min-height: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #333;
            flex-grow: 1;
            line-height: 1.7;
            letter-spacing: 0.3px;
        }}
        
        @media print {{
            body {{
                background-color: white;
            }}
            .page {{
                box-shadow: none;
                margin: 0;
                padding: 20px;
            }}
            .comic-panel {{
                box-shadow: none !important;
                transform: none !important;
            }}
        }}
        
        @media (max-width: 768px) {{
            .comic-grid {{
                grid-template-columns: 1fr;
            }}
            .page {{
                padding: 20px;
            }}
            .hero-panel {{
                grid-column: span 1;
                grid-row: span 1;
            }}
        }}
    </style>
</head>
<body>
{pages}
</body>
</html>"""

    # Create pages
    pages_html = []
    
    # First page has hero panel (4 spaces) + 8 regular panels = 12 spaces
    # Subsequent pages have 12 regular panels
    panel_index = 0
    page_num = 0
    
    while panel_index < len(panels):
        # Page title
        if lang == 'es':
            page_title = f"{titles.get(lang, 'Historieta')} - Página {page_num + 1}"
        elif lang == 'ru':
            page_title = f"{titles.get(lang, 'История')} - Страница {page_num + 1}"
        else:
            page_title = f"{titles.get(lang, 'Comic')} - Page {page_num + 1}"
        
        page_html = f'''    <div class="page">
        <h1 class="page-header">{page_title}</h1>
        <div class="comic-grid">
'''
        
        if page_num == 0:
            # First page: 1 hero panel + 8 regular panels
            # Hero panel (first image)
            if panel_index < len(panels):
                panel = panels[panel_index]
                caption = panel.get(lang, panel.get('en', 'No description'))
                page_html += f'''            <div class="comic-panel hero-panel">
                <img src="{panel['filename']}" alt="{caption[:50]}..." class="panel-image">
                <div class="panel-caption">{caption}</div>
            </div>
'''
                panel_index += 1
            
            # Regular panels for the rest of the first page
            panels_on_page = 8
        else:
            # Other pages: 12 regular panels
            panels_on_page = 12
        
        # Add regular panels
        for i in range(panels_on_page):
            if panel_index < len(panels):
                panel = panels[panel_index]
                caption = panel.get(lang, panel.get('en', 'No description'))
                
                # Check if this is the last panel
                if panel_index == len(panels) - 1:
                    # Make the last panel a hero panel
                    page_html += f'''            <div class="comic-panel hero-panel">
                <img src="{panel['filename']}" alt="{caption[:50]}..." class="panel-image">
                <div class="panel-caption">{caption}</div>
            </div>
'''
                else:
                    # Regular panel
                    page_html += f'''            <div class="comic-panel">
                <img src="{panel['filename']}" alt="{caption[:50]}..." class="panel-image">
                <div class="panel-caption">{caption}</div>
            </div>
'''
                panel_index += 1
        
        page_html += '''        </div>
    </div>
'''
        pages_html.append(page_html)
        page_num += 1
    
    # Language codes
    lang_codes = {'es': 'es', 'en': 'en', 'ru': 'ru'}
    
    return html_template.format(
        lang_code=lang_codes.get(lang, 'en'),
        title=titles.get(lang, 'Comic'),
        pages='\n'.join(pages_html)
    )

def main():
    # Parse the markdown file
    titles, panels = parse_markdown('story.md')
    
    # Generate HTML for each language
    languages = ['es', 'en', 'ru']
    
    for lang in languages:
        html_content = generate_html(titles, panels, lang)
        output_file = f'historieta.{lang}.html'
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Generated: {output_file}")

if __name__ == "__main__":
    main()