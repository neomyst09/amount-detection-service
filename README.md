# Amount Detection Service

A FastAPI-based OCR service that extracts monetary amounts (Total, Paid, Due) from bill/receipt images.

## Features
- OCR text extraction from bill images
- Numeric token normalization
- Intelligent classification of Total, Paid, and Due amounts
- REST API with Swagger UI

## Tech Stack
- Python 3.13
- FastAPI
- Uvicorn
- Pillow
- pytesseract
- Regex-based NLP

## API Endpoint

### POST /detect-amounts
Accepts an image file and returns detected amounts.

**Request**
- multipart/form-data
- file: image/jpeg or image/png

**Response**
```json
{
  "raw_text": "...",
  "numbers": [661.5, 500, 161.5],
  "amounts": {
    "total": 661.5,
    "paid": 500,
    "due": 161.5
  },
  "confidence": 0.75
}
