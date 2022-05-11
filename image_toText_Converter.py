from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image = 'images/contact.png'
text = pytesseract.image_to_string(Image.open(image), lang="eng")
print(text)