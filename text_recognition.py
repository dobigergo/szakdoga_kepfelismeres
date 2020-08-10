import cv2
import numpy as np
import pytesseract
import falcon

def filter_empty_strings(word):
    empty = ['',' ', '/n']
    
    if word in empty:
        return False
    else:
        return True

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread("orvosi-tablazat-1.jpg")

length, width, dim = np.shape(img)

img_hun = img[0:length, 0:width//2]
img_eng = img[0:length, width//2:width]

text_eng = pytesseract.image_to_string(img_eng)
text_hun = pytesseract.image_to_string(img_hun, lang = "hun")

text_hun_set = list(filter(filter_empty_strings,text_hun.split("\n")))
text_eng_set = list(filter(filter_empty_strings,text_eng.split("\n")))

print(text_hun_set)
print(text_eng_set)

