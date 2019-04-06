#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Xie1
# @Time: 19-4-6 21:04
# @File: p04_sina.py

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

response = requests.get('https://www.sina.com.cn', headers=headers)

print(response.content.decode())
print('a'*50)
print(response.text)   # 乱码

