import time
from urllib import request

import pytesseract
from PIL import Image


def main():
    pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'
    while True:
        url = 'https://e.coding.net/api/getCaptcha'
        request.urlretrieve(url, 'captcha.png')
        image = Image.open('captcha.png')
        text = pytesseract.image_to_string(image)
        print(text)
        time.sleep(2)

if __name__ == "__main__":
    main()
