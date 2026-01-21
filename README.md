# Amount Detection Service

OCR-based receipt amount detection using FastAPI.

## Features
- Extracts text from receipt images using Tesseract OCR
- Normalizes noisy OCR numeric output
- Detects Total, Paid, and Due amounts
- REST API with FastAPI

## Tech Stack
- Python
- FastAPI
- Tesseract OCR
- Pillow
- Regex-based text processing

## Installation
```bash
pip install -r requirements.txt
