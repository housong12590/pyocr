from PIL import ImageGrab
import base64
from io import BytesIO

import win32clipboard as w
import win32con

import pyperclip
from ctypes import *


def image_to_base64():
    img = ImageGrab.grabclipboard()
    output_buffer = BytesIO()
    img.save(output_buffer, format='JPEG')
    byte_data = output_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    return base64_str
