# File Directory Organizer

> Automatically sort your messy folders with Python

---

## Overview

The File Directory Organizer is a Python script that automatically scans a target folder and sorts all files into clearly named subfolders based on their file type. No more hunting through cluttered Downloads folders — one command and everything is in its place.

---

## Features

- Automatic categorization into Images, Documents, Archives, Media, and Executables
- Handles unknown file types gracefully by placing them in an `Others` folder
- Duplicate file protection — appends `_copy` to avoid overwriting existing files
- Clear console output showing every file moved, renamed, or skipped
- Safe test environment setup via a companion setup script

---

## Project Structure

```
├── organizer.py       # Main script — scans and moves files
└── setup_test.py      # Helper script — creates a test folder with dummy files
```

---

## File Categories

| Category    | File Extensions                                      |
|-------------|------------------------------------------------------|
| Images      | `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`              |
| Documents   | `.pdf`, `.docx`, `.doc`, `.txt`, `.xlsx`, `.pptx`, `.csv` |
| Archives    | `.zip`, `.rar`, `.tar`, `.gz`                        |
| Media       | `.mp4`, `.mp3`, `.mkv`, `.wav`                       |
| Executables | `.exe`, `.msi`, `.dmg`                               |
| Others      | Any unrecognized extension                           |

---

## Getting Started

### Prerequisites

- Python 3.6 or higher
- No external libraries required — uses only the built-in `os` and `shutil` modules

### Step 1: Create a Test Environment (Recommended)

Before running the organizer on any real folder, use the setup script to create a safe sandbox:

```bash
python setup_test.py
```

This creates a `test_folder/` directory in the same location as the script and populates it with 11 dummy files covering all supported categories.

### Step 2: Run the Organizer

```bash
python organizer.py
```

By default, the script targets `./test_folder`. To change the target, open `organizer.py` and update this line at the bottom:

```python
folder_to_organize = "./test_folder"   # Change this to your target path
```

### Step 3: Review the Output

```
Scanning directory: ./test_folder...

✅ Moved: biology_notes.txt -> Documents/
✅ Moved: monthly_budget.csv -> Documents/
✅ Moved: profile_pic.jpg -> Images/
✅ Moved: podcast_episode.mp3 -> Media/
⚠️  Duplicate found! Renaming 'report.pdf' to 'report_copy.pdf'

🎉 Organization complete!
```

---

## How It Works

1. Defines a category map linking each file extension to a folder name.
2. Verifies the target directory exists before proceeding.
3. Iterates over every item in the directory, skipping subfolders.
4. Checks for duplicate filenames at the destination and renames with `_copy` if needed.
5. Moves the file using `shutil.move()` and logs the result to the console.

---

## Customization

### Adding New File Types

Open `organizer.py` and find the `categories` dictionary. Add extensions to an existing category or create a new one:

```python
categories = {
    "Images":    ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
    "Code":      ['.py', '.js', '.html', '.css', '.ts'],  # New category
    ...
}
```

### Changing the Target Directory

Pass any absolute or relative path to `organize_directory()` at the bottom of `organizer.py`:

```python
folder_to_organize = "/Users/yourname/Downloads"
```

---

## Safety Notes

> ⚠️ **Always test the script on a copy of your data before running it on your real files.** File moves via `shutil.move()` are not automatically reversible.

- The script only moves files — it never deletes anything.
- Subfolders inside the target directory are left untouched.
- The `_copy` suffix prevents any data loss from filename collisions.

---
