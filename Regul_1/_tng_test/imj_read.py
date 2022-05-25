import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image

image = cv2.imread("ex.PNG")
#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\a.ershov\AppData\Local\Tesseract-OCR\tesseract.exe'
tessdata_dir_config = r'--oem 3 --psm 6 --tessdata-dir "C:\Users\a.ershov\AppData\Local\Tesseract-OCR\tessdata"'
string = pytesseract.image_to_string(image, lang='rus', config=tessdata_dir_config)
# печатаем
print(string)