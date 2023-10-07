# HandwrittenToText
# OCR Project

## Overview

This project is focused on Optical Character Recognition (OCR), a technology that extracts text from images. The goal is to provide a simple and flexible OCR solution using Python and popular libraries.
## Credit 
-made by CTRL-ALT-CODE at junction X Algiers 
Team : Anes , Mehdi ,Willem , Sidali
## Features

- Real-time OCR from webcam feed.
- Support for image-based OCR on local files.
- Integration with Tesseract OCR engine.
- User-friendly web app for image upload and OCR.

## Dependencies

- OpenCV: `pip install opencv-python`
- Pillow (PIL): `pip install Pillow`
- Tesseract OCR: Follow [Tesseract installation instructions](https://github.com/tesseract-ocr/tesseract).

## Setup

1. Install dependencies using `pip install -r requirements.txt`.
2. Configure Tesseract path in the script (`pytesseract.pytesseract.tesseract_cmd`).

## Usage

### Real-time OCR

Run the script `realtime_ocr.py` to perform OCR on the live webcam feed.

```bash
python realtime_ocr.py
