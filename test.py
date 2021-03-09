# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2021/2/27 10:21
# @Author  : Mr.V
# @FileName: test.py
# @Software: PyCharm
"""


# import requests

# url = "https://www.baidu.com"
# resp = requests.get(url)
# print("baidu")
# url = "https://github.com/fatedier/frp/releases/download/v0.35.1/frp_0.35.1_windows_amd64.zip"
# resp = requests.get(url, stream=True)
# print("ok")
# print(int(resp.headers['content-length']))
# with open("frp.zip", "wb") as f:
#     f.write(resp.content)

import requests

# save_path = r"C:\Users\Mr.V\Desktop\frp\frp.zip"
# def download_url(url, chunk_size=4096):
#     global save_path
#     r = requests.get(url, stream=True)
#     print(int(r.headers['content-length']))
#     with open(save_path, 'wb') as fd:
#         for i, chunk in enumerate(r.iter_content(chunk_size=chunk_size)):
#             print(i+1)
#             fd.write(chunk)
# download_url(url)

import os
import sys

# insert path of this script in syspath so actions.py will be found
# sys.path.insert(1, os.path.dirname(os.path.abspath(__file__)))

#
# This is exactly like issuing the command:
#  $ rasa run actions
#
# sys.argv.append('shell')
# sys.argv.append('actions')
# print("pre")
# from rasa.__main__ import main
# print("ok")
# main()

from rasa.run import run


run("./models", "./endpoints.yml", port=8001)


