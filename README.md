# Mahjong Hand Helper - Setup and Usage Guide

A Python application that helps you identify the best possible Mahjong hands from your current tiles based on official rules. This tool displays tiles visually and suggests the top 3 potential hands you can form.

## I'll be so real with you tkinter is fun for quick and dirty prototypes but:

Here's a web script version as well (you can skip the rest of this README now) https://lxwooxy.github.io/mahjong.html

## Prerequisites

- Python 3.7 or higher installed on your computer
- Git (for cloning the repository)
- Basic familiarity with terminal/command prompt

## Installation Steps

### 1. Clone the Repository

Open your terminal (Mac/Linux) or Command Prompt (Windows) and run:

```bash
git clone <repository-url>
cd mahjong
```

Replace `<repository-url>` with the actual URL of this repository.

### 2. Install Required Libraries

The application requires the following Python libraries:
- `tkinter` (usually comes pre-installed with Python)
- `Pillow` (for image handling)

Install the required library using pip:

```bash
pip install Pillow
```

**Note for macOS users:** If you're using Python 3 specifically, you may need to use `pip3` instead:

```bash
pip3 install Pillow
```

**Note:** `tkinter` comes bundled with most Python installations. If you encounter an error about tkinter being missing, you may need to install it separately:
- **Ubuntu/Debian:** `sudo apt-get install python3-tk`
- **Fedora:** `sudo dnf install python3-tkinter`
- **macOS:** It should be included with Python from python.org

### 3. Verify Tile Images

The repository should already include an `images` folder with all the necessary Mahjong tile images. Verify that the folder exists and contains the following files:
- Bamboo tiles: `1bam.png` through `9bam.png`
- Character tiles: `1crack.png` through `9crack.png`
- Dot tiles: `1dot.png` through `9dot.png`
- Wind tiles: `east.png`, `south.png`, `west.png`, `north.png`
- Dragon tiles: `reddragon.png`, `greendragon.png`, `soap.png`
- Special tiles: `flower.png`, `joker.png`

**Note:** If the images folder is missing, you'll need to create it and add the tile images with the naming convention above.

## Running the Application

### From Terminal/Command Prompt

Navigate to the directory containing the script and run:

```bash
python mahjong.py
```

Or on some systems:

```bash
python3 mahjong.py
```

## How to Use the Application

### 1. **Select Your Tiles**
   - The left panel displays all available Mahjong tiles organized by category (Bamboo, Character, Dot, Winds, Dragons, Special)
   - Click on any tile image to add it to your hand
   - You can add the same tile multiple times by clicking it again

### 2. **View Your Hand**
   - Your selected tiles appear in the "Your Hand" listbox
   - Tiles are listed in the order you selected them

### 3. **Remove Tiles (if needed)**
   - Click on each tile in the "Your Hand" listbox to remove them
   - Click the **"Clear All"** button to remove all tiles and start over

### 4. **Find Best Hands**
   - Once you've selected your tiles, click the **"Find Best Hands"** button
   - The application will analyze your tiles and display the top 3 potential hands

### 5. **Understanding the Results**
   Each suggested hand shows:
   - **Hand Name**: The official name of the Mahjong hand
   - **Points Value**: How many points the hand is worth
   - **Progress**: How many tiles you have vs. how many are needed
   - **The Line**: Visual representation of the complete hand pattern
   - **What You Have**: Shows which tiles you currently have (using abbreviations)
     - Regular tiles are shown with their abbreviation
     - `J` indicates where a Joker is being used
     - `_` indicates missing tiles
   - **Missing**: Lists exactly which tiles you still need to complete the hand

## Tile Abbreviations Used in Results

- Numbers with suit: `1B`, `2C`, `3D` (Bamboo, Character, Dot)
- Winds: `N`, `E`, `W`, `S` (North, East, West, South)
- Dragons: `D` (all dragon types)
- Flower: `F`
- Joker: `J`

## Tips

1. **Jokers are Smart**: The application automatically uses your Jokers optimally to complete sets of 3+ matching tiles
2. **Multiple Hands**: If you're close to completing multiple hands, the top 3 are ranked by both progress and point value
3. **Experiment**: Try adding different tile combinations to explore various hand possibilities

## Troubleshooting

### "Module not found" errors
- Make sure you've installed Pillow: `pip install Pillow`
- Ensure you're using the correct Python version

### Tile images not appearing
- Verify that the `images` folder exists in the same directory as the script
- Check that all image files are named correctly (case-sensitive on Mac/Linux)
- The application will show text buttons as fallback if images are missing

### Application won't start
- Confirm Python 3.7+ is installed: `python --version`
- Check that tkinter is installed (try importing it in Python: `python -c "import tkinter"`)

## Project Structure
```
mahjong/
│
├── mahjong.py          # Main application file (GUI)
├── rules.py            # Mahjong hand definitions and rules
├── images/             # Folder containing tile images
│   ├── 1bam.png
│   ├── 2bam.png
│   └── ... (all tile images)
└── README.md          # This file
```

## Support

If you encounter any issues, please check that:
1. All dependencies are correctly installed
2. The images folder contains all required tile images
3. You're using a compatible Python version (3.7+)

Enjoy playing Mahjong! 🀄