from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def image_to_text(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)

        return text
    except Exception as e:
        print(f"Error processing image: {str(e)}")
