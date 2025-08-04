# CLAUDE.md - Project Documentation for AI Assistant

## Project Overview

This is a multilingual children's story project featuring Mr. Pinpin and Mr. PomPom, two hedgehog brothers who help a wise owl recover his lost glasses.

## Characters

- **Mr. Pinpin**: Hedgehog with blue wizard hat and magical wand (protagonist)
- **Mr. PomPom**: Hedgehog with red hat, Mr. Pinpin's brother
- **Wise Owl**: A scholarly owl who loses his glasses and needs help

## Project Structure (Multi-Chapter)

```
mr pinpin recover owl glasses/
├── index.html                    # Main chapter selection page
├── storyline.md                  # Overall series narrative and planning
├── README.md                     # GitHub repository documentation
├── CLAUDE.md                     # This file - AI assistant reference
├── .gitignore                    # Git ignore file
└── chapter1/                     # Chapter 1: The Quest for the Owl's Glasses
    ├── index.html               # Language selection for this chapter
    ├── story.md                 # Source story in all languages
    ├── generate_historieta.py   # Script to generate HTML from markdown
    ├── historieta.es.html       # Spanish version
    ├── historieta.en.html       # English version
    ├── historieta.ru.html       # Russian version
    └── [20 PNG files]          # Story illustrations (02_Screenshot...png through 21_Screenshot...png)

Future chapters will follow the same structure in chapter2/, chapter3/, etc.
```

## Key Technical Details

### Story Format
- **Layout**: 2-column comic book grid
- **Hero Panels**: First and last images occupy 2x2 grid spaces
- **Regular Panels**: All other images are 1x1 grid space
- **Captions**: Each panel has narrative text below the image
- **Languages**: Spanish (es), English (en), Russian (ru)

### Design Specifications
- **Fonts**: Kalam (primary), Comic Neue, Comic Sans MS (fallbacks)
- **Background**: Light grey (#f5f5f5) for page, grey (#f9f9f9) for panels
- **Panel Style**: Rounded corners (8px), subtle shadows, hover effects
- **Responsive**: Adapts to mobile (single column below 768px)

## Workflow

### To Generate HTML Files for a Chapter:

```bash
# Navigate to the specific chapter folder
cd "/Users/miguel_lemos/Desktop/mr pinpin recover owl glasses/chapter1"
python3 generate_historieta.py
```

This will create/update:
- historieta.es.html
- historieta.en.html
- historieta.ru.html

### To Add a New Chapter:

1. Create new chapter folder: `mkdir chapter2`
2. Copy generator script: `cp chapter1/generate_historieta.py chapter2/`
3. Create `story.md` with the new story content
4. Add images (PNG files) to the chapter folder
5. Create `index.html` for language selection
6. Update root `index.html` to link to new chapter
7. Update `storyline.md` with chapter status

### To Test Locally:

```bash
# Open the main landing page
open index.html

# Or open a specific language version
open historieta.en.html
```

### To Deploy Changes:

```bash
# Add all changes
git add .

# Commit with descriptive message
git commit -m "Your commit message"

# Push to GitHub
git push origin main
```

The site auto-deploys to: https://miguelemosreverte.github.io/MrPinPin/

## Story Structure

### Panel Organization:
1. **Page 1**: 1 hero panel (2x2) + 8 regular panels = 9 panels total
2. **Page 2**: 10 regular panels + 1 hero panel (2x2) = 11 panels total

### Important Notes:
- First image (02_Screenshot) is the opening hero panel
- Last image (21_Screenshot) is the closing hero panel
- We deleted 01_Screenshot as it was a test image
- Images are numbered 02-21 (20 images total)

## How to Edit the Story

### To modify text:
1. Edit `story.md` file
2. Each panel has three language versions (es, en, ru)
3. Run `python3 generate_historieta.py` to regenerate HTML files

### To modify styling:
1. Edit CSS in `generate_historieta.py`
2. Regenerate HTML files
3. Test responsiveness on different screen sizes

### To add a new language:
1. Add translations to each panel in `story.md`
2. Update language arrays in `generate_historieta.py`
3. Add language button to `index.html`
4. Regenerate HTML files

## Common Tasks

### Update panel text:
```python
# In story.md, find the panel and update the relevant language line:
- es: [Spanish text]
- en: [English text]
- ru: [Russian text]
```

### Change hero panel:
```python
# In generate_historieta.py, modify the logic that checks:
if panel_index == 0:  # First panel
if panel_index == len(panels) - 1:  # Last panel
```

### Adjust layout:
```python
# In generate_historieta.py, modify CSS grid:
grid-template-columns: repeat(2, 1fr);  # 2 columns
gap: 25px;  # Space between panels
```

## GitHub Repository

- **URL**: https://github.com/miguelemosreverte/MrPinPin
- **Live Site**: https://miguelemosreverte.github.io/MrPinPin/
- **Main Branch**: main
- **Auto-deploy**: GitHub Pages from main branch

## Testing Checklist

Before pushing changes:
- [ ] Test all three language versions
- [ ] Check responsive design on mobile
- [ ] Verify hero panels display correctly
- [ ] Ensure all images load
- [ ] Test language selection on index.html
- [ ] Confirm captions are readable
- [ ] Check for console errors

## Future Enhancements Ideas

1. Add audio narration for each panel
2. Create PDF versions for printing
3. Add more languages
4. Implement page turn animations
5. Create character profile pages
6. Add sound effects for magical moments
7. Create coloring book version

## Project History

- Created: August 2025
- Original concept: Help an owl find his glasses
- Setting: Morning in the Enchanted Forest
- Theme: Friendship, helping others, magic
- Target audience: Children learning to read

## Important Context for Future Sessions

- This is a complete, working project
- All files are already on GitHub
- The story emphasizes kindness and friendship
- Mr. Pinpin's magic works best when helping others
- The visual style should remain child-friendly and whimsical
- Keep the comic book aesthetic with the historieta styling