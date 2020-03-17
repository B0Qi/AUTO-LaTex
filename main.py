import keyboard
from mathpix.mathpix import MathPix
import json
import clipboard as c
from PyQt5.QtWidgets import QApplication
import os 

img_list = ['jpg', 'jpeg', 'png']

config = {}
with open('config.json','r') as f:
    config = json.load(f) 

mathpix = MathPix(app_id=config['app_id'], app_key=config['app_key'])
app = QApplication([])
clipboard = app.clipboard()

ALT = False
C = False


def process():
    # try:
    data = clipboard.mimeData() 
    if data.hasImage():
        print("Image Detected!")
        image = clipboard.pixmap()
        image.save('temp.png')
        try:
            ocr = mathpix.process_image(image_path='./temp.png')
            print("OCR confidence is " + str(ocr.latex_confidence))
            c.copy(ocr.latex)
            os.remove('temp.png')
        except Exception as e:
            print(e)
            c.copy("Nothing is detected!")
            if os.path.exists('temp.png'):
                os.remove('temp.png')
    elif clipboad.mimeData.hasText():
        print("Text detected!")
        text = clipboad.mimeData.text()
        if "/" in tmp_text:
            tmp_text = tmp_text.split("/")[-1]
            if "." in tmp_text:
                tmp_text = tmp_text.split(".")[-1]
                if tmp_text in img_list:
                    print('Image might be detected!')
                else:
                    print(text)
    else:
        print("No Image detected in clipboard.")
        c.copy("No Image detected in clipboard.")        



def main():
    keyboard.add_hotkey('ctrl+alt+m',process)
    keyboard.wait()

main()