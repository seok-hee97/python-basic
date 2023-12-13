import io
import pyautogui
from base64 import b64encode
import requests


KEY_IMG_BB ="dfa808d7dee667d55d7532562df016ca"
IMG_BB_URL ="https://api.imgbb.com/1/upload"
screenshot=pyautogui.screenshot()


img_bytes = io.BytesIO()
screenshot.save(img_bytes, format="PNG")
img_bytes=img_bytes.getvalue()
img_encoded = b64encode(img_bytes)
payload = {"key": KEY_IMG_BB, "image":img_encoded}
res = requests.post(IMG_BB_URL, payload)
print(res.ok)

# import io
# import pyautogui
# from base64 import b64encode
# import requests

# KEY_IMG_bb = "dfa808d7dee667d55d7532562df016ca"
# IMG_BB_URL = "https://api.imgbb.com/1/upload"

# screenshot = pyautogui.screenshot()

# img_bytes = io.BytesIO()
# screenshot.save(img_bytes, format="PNG")
# img_bytes = img_bytes.getvalue()
# img_encoded = b64encode(img_bytes)
# payload = {"key":KEY_IMG_bb, "image":img_encoded}
# res = requests.post(IMG_BB_URL, payload)
# print(res.ok)