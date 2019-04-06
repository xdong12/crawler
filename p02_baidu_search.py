#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Xie1
# @Time: 19-4-6 20:33
# @File: p02_baidu_search.py

import requests
# 输入要搜索的内容
word = input('请求输入要搜索的内容: ')
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

# 1. 拼接URL
# url = 'https://www.baidu.com/s?wd={}'.format(word)
# response = requests.get(url, headers=headers)
# print(response.content.decode())

# 2. 使用params的参数
# 准备URL: ? 前面的
url = 'https://www.baidu.com/s'
# 准备参数字典
params = {
    'wd': word
}

# 发送请求, 获取响应
response = requests.get(url, params=params, headers=headers)
print(response.content.decode())