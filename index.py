from pyhk import key, start, add_hot_key
from PIL import ImageGrab
from aip import AipOcr
from pyperclip import copy,paste

APP_ID = '15168527'
API_KEY = '9FGI83E5syxRZObIKZXeignm'
SECRET_KEY = "V5D3qmcMnBRwgc0l3yryHyWHImpVKw4T"

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def call():
    try:
        img = ImageGrab.grabclipboard()
        if img is None:
            return
        img.save('screenshot.png')
        f = open('screenshot.png', 'rb')
        image = f.read()
        f.close()
        resp = client.basicGeneral(image)
        for item in resp.get('words_result'):
            text = item.get("words")
            copy(text)
            paste()
            print(text)
    except Exception as e:
        print(e)


add_hot_key([key.ctrl_l, key.f1], call)
if __name__ == '__main__':
    start()
