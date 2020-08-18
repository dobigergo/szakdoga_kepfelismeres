from PIL import Image
import numpy as np
import pytesseract
import falcon
import json

def filter_empty_strings(word):
    empty = ['',' ', '/n']
    
    if word in empty:
        return False
    else:
        return True
        
class TranslationEntries:
    
    word1 = ""
    word2 = ""
    
    def __init__(self,word1,word2):
        self.word1 = word1
        self.word2 = word2


def make_json(wordList1, wordList2):
    
    translationList = []
    for i in range(len(wordList1)):
        translationList.add(TranslationEntries(wordList1[i],wordList2[i]))
        
        
    return json.dumps(translationList)
    
class Response:

    def on_get(self,req,resp):
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

        img = Image.open('orvosi-tablazat-1.jpg')

        length, width, dim = np.shape(img)

        img_hun = img[0:length, 0:width//2]
        img_eng = img[0:length, width//2:width]

        text_eng = pytesseract.image_to_string(img_eng)
        text_hun = pytesseract.image_to_string(img_hun, lang = "hun")

        text_hun_set = list(filter(filter_empty_strings,text_hun.split("\n")))
        text_eng_set = list(filter(filter_empty_strings,text_eng.split("\n")))
        
        resp.body = make_json(text_hun_set,text_eng_set)

       
api = falcon.API()
response = response()
api.add_route('/', response)
