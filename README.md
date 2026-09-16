# Multimedia Analyzer

A Python-based project for extracting metadata from multimedia files.

## Task 1 — Image Analyzer

The Image Analyzer extracts metadata from image files using the Pillow library.

### Supported Formats

* JPG
* JPEG
* PNG

### Extracted Information

* File Name
* File Size
* File Format
* Width
* Height
* Resolution
* Color Mode
* Camera information
* Date Taken
* Orientation

## Project Structure

```text
multimedia_analyzer/
│
├── image_analyzer.py
├── README.md
│
└── samples/
    ├── image.jpg
    └── image.png
```

## Requirements

Python 3.x

Install Pillow:

```bash
python -m pip install Pillow
```

## How to Run

Open the terminal in the project folder and run:

```bash
python image_analyzer.py
```

Enter the image path when asked:

```text
samples/image.jpg
```

## Example Output

```text
================================
IMAGE METADATA REPORT
================================
File Name       : image.jpg
File Size       : 26535 bytes
File Format     : JPEG
Width           : 506
Height          : 900
Resolution      : (96, 96)
Color Mode      : RGB

EXIF Metadata
-------------------------------
Camera          : Not available
Date Taken      : Not available
Orientation     : Not available
```

## Technology Used

Python

Pillow
