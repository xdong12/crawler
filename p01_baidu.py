#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Xie1
# @Time: 19-4-6 19:34
# @File: p01_baidu.py

import requests

# 2. 发送请求, 获取响应
response = requests.get('http://www.baidu.com')

# 3. 获取响应数据
# response.encoding = 'utf8'
# 获取解码使用的字符集
# print(response.encoding) # ISO-8859-1: 西欧字符集; 根据响应头推断出来的.
# 3.1 text: 获取响应的字符串数据
# print(response.text)
# 获取响应二进制数据
# print(response.content)
print(response.content.decode())

with open('html/p01_baidu_1.html', 'wb') as f:
    f.write(response.content)

# # 更多属性
# print(response.status_code)
# print(response.headers)
# print(response.url)
# # 请求URL
# print(response.request.url)
# print(response.request.headers)


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

response2 = requests.get('http://www.baidu.com', headers=headers)

with open('html/p01_baidu_2.html', 'wb') as f:
    f.write(response2.content)
