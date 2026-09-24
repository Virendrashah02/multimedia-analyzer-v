# Multimedia Analyzer

A Python-based project for extracting metadata from multimedia files.

This project is being developed step-by-step:

1. Image Analyzer
2. Video Analyzer
3. Audio Analyzer
4. Consolidated Multimedia Analyzer

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
* Camera
* Date Taken
* Orientation

---

# Task 2 — Video Analyzer

The Video Analyzer extracts technical metadata from video files using FFmpeg and FFprobe.

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

* Metadata tags
* Creation time
* Format information

---

# Task 3 — Audio Analyzer

The Audio Analyzer extracts technical and metadata information from audio files using FFmpeg and FFprobe.

## Extracted Information

### General

* File Name
* File Size
* Format
* Duration

### Audio

* Codec
* Channels
* Sampling Rate
* Bit Rate

### Metadata

* Title or other available tags
* Artist or other available tags
* Album or other available tags
* Encoder
* Date
* BPM
* Other available metadata

## Example Output

```text
================================
AUDIO METADATA REPORT
================================
File Name       : song.mp3
File Size       : 1059386 bytes
Format          : mp3
Duration        : 00:00:57

AUDIO
--------------------------------
Codec           : mp3
Channels        : 2
Sampling Rate   : 44100 Hz
Bit Rate        : 146.06 kbps

METADATA
--------------------------------
Encoded by              : LAME in FL Studio 20
BPM (beats per minute)  : 120
date                    : 2018
encoder                 : LAME3.100
```

---

# Project Structure

```text
multimedia_analyzer/
│
├── image_analyzer.py
├── video_analyzer.py
├── audio_analyzer.py
├── README.md
├── .gitignore
│
└── samples/
    ├── image.jpg
    ├── image.png
    ├── video.mp4
    └── song.mp3
```

---

# Requirements

## Python

Python 3.x

## Pillow

Install Pillow:

```bash
python -m pip install Pillow
```

## FFmpeg and FFprobe

FFmpeg and FFprobe must be installed and available in the system PATH.

Check FFmpeg:

```bash
ffmpeg -version
```

Check FFprobe:

```bash
ffprobe -version
```
