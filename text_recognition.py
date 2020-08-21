import cv2
import numpy as np
import pytesseract
import flask
import json


app = Flask(__name__)

def filter_empty_strings(word):
    empty = ['',' ', '/n']
    
    if word in empty:
        return False
    else:
        return True
        

def make_json(wordList1, wordList2):
    
    translationList = []
    for i in range(len(wordList1)-1):
        resultDict = {}
        resultDict["word1"]=wordList1[i]
        resultDict["word2"]=wordList2[i]
        translationList.append(resultDict)
            
    return json.dumps(translationList, ensure_ascii=False).encode('utf8')
    
@app.route('/')
def on_get():
        
    pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'

    img = cv2.imread('orvosi-tablazat-1.jpg')

    length, width, dim = np.shape(img)
    img_hun = img[0:length, 0:width//2]
    img_eng = img[0:length, width//2:width]
    text_eng = pytesseract.image_to_string(img_eng, lang= "eng")
    text_hun = pytesseract.image_to_string(img_hun, lang = "hun")
    text_hun_set = list(filter(filter_empty_strings,text_hun.split("\n")))
    text_eng_set = list(filter(filter_empty_strings,text_eng.split("\n")))
    
    return make_json(text_hun_set,text_eng_set)
