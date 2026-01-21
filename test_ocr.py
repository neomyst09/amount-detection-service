from PIL import Image
from app.ocr import extract_text_from_image

img = Image.open("samples/sample_bill.jpg")
result = extract_text_from_image(img)

print(result)
