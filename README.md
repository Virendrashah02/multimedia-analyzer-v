# Multimedia Analyzer

A Python-based project for extracting metadata from multimedia files.

This project is being developed step-by-step as part of three tasks:

1. Image Analyzer
2. Video Analyzer
3. Audio Analyzer

The final goal is to combine all three analyzers into one Consolidated Multimedia Analyzer.

---

# Task 1 — Image Analyzer

The Image Analyzer extracts metadata from image files using the Pillow library.

## Supported Formats

* JPG
* JPEG
* PNG

## Extracted Information

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

---

# Task 2 — Video Analyzer

The Video Analyzer extracts technical metadata from video files using FFmpeg/FFprobe.

## Extracted Information

### General

* File Name
* File Size
* Container
* Duration

### Video

* Resolution
* Frame Rate
* Bit Rate
* Codec

### Audio

* Codec
* Channels
* Sampling Rate
* Bit Rate

### Metadata

* Video metadata tags
* Creation time
* Format information

## Example Output

```text
================================
VIDEO METADATA REPORT
================================
File Name       : video.mp4
File Size       : 8641056 bytes
Container       : mov,mp4,m4a,3gp,3g2,mj2
Duration        : 00:00:16

VIDEO
--------------------------------
Resolution      : 1280x720
Frame Rate      : 14.99 FPS
Bit Rate        : 4.02 Mbps
Codec           : h264

AUDIO
--------------------------------
Codec           : aac
Channels        : 2
Sampling Rate   : 48000 Hz
Bit Rate        : 162.27 kbps

METADATA
--------------------------------
major_brand         : mp42
minor_version       : 0
compatible_brands   : mp41isom
creation_time       : 2026-09-08T09:17:41.000000Z
```

---

# Project Structure

```text
multimedia_analyzer/
│
├── image_analyzer.py
├── video_analyzer.py
├── README.md
├── .gitignore
│
└── samples/
    ├── image.jpg
    ├── image.png
    └── video.mp4
```

---

# Requirements

## Python

Python 3.x

## Image Analyzer

Install Pillow:

```bash
python -m pip install Pillow
```

## Video Analyzer

FFmpeg and FFprobe must be installed and available in the system PATH.

Check installation:

```bash
ffmpeg -version
```

```bash
ffprobe -version
```

---

# How to Run

## Image Analyzer

```bash
python image_analyzer.py
```

Enter the image path:

```text
samples/image.jpg
```

## Video Analyzer

```bash
python video_analyzer.py
```

Enter the video path:

```text
samples/video.mp4
```

---

# Technologies Used

* Python
* Pillow
* FFmpeg
* FFprobe

---

# Future Tasks

## Task 3 — Audio Analyzer

The Audio Analyzer will extract metadata such as:

* File Name
* File Size
* Format
* Duration
* Codec
* Channels
* Sampling Rate
* Bit Rate
* Title
* Artist
* Album
* Genre

## Final Project — Consolidated Multimedia Analyzer

The final application will automatically identify whether the input file is:

```text
IMAGE
AUDIO
VIDEO
```

and then call the appropriate analyzer.

Planned structure:

```text
User Input
    ↓
File Validation
    ↓
Identify File Type
    ↓
Image / Audio / Video Analyzer
    ↓
Metadata Extraction
    ↓
Report Generator
    ↓
Consolidated Report
```
