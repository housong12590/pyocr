from aip import AipOcr
# from .index import image_to_base64
from PIL import ImageGrab
import base64
from io import BytesIO


# https://www.cnblogs.com/dcb3688/p/4496934.html

def image_to_base64():
    img = ImageGrab.grabclipboard()
    img.save('test.png')
    # output_buffer = BytesIO()
    # img.save(output_buffer, format='PNG')
    # byte_data = output_buffer.getvalue()
    # base64_str = base64.b64encode(byte_data)
    # return base64_str


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# image_to_base64()

# image = get_file_content('test.png')

APP_ID = '15168527'
API_KEY = '9FGI83E5syxRZObIKZXeignm'
SECRET_KEY = "V5D3qmcMnBRwgc0l3yryHyWHImpVKw4T"

# client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
#
# resp = client.basicGeneral(image)
# print(resp)
# for item in resp.get('words_result'):
#     text = item.get("words")
#     print(text)

import win32serviceutil

import win32service

import win32event


class PythonService(win32serviceutil.ServiceFramework):
    # 服务名

    _svc_name_ = "weater"

    # 服务显示名称

    _svc_display_name_ = "weater"

    # 服务描述

    _svc_description_ = "天气服务"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)

        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

        self.isAlive = True

    def SvcDoRun(self):
        print("----------")

    def SvcStop(self):
        # 先告诉SCM停止这个过程

        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)

        # 设置事件

        win32event.SetEvent(self.hWaitStop)

        self.isAlive = False


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(PythonService)
