#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Xie1
# @Time: 19-4-7 14:46
# @File: p05_iciba.py

import sys
import requests
import json

# 获取要翻译的内容
word = input('输入要翻译的内容:')
# 翻译的URL
url = 'http://fy.iciba.com/ajax.php?a=fy'

# 准备数据
data = {
    'f': 'auto',
    't': 'auto',
    'w': word
}

# 发送请求
response = requests.post(url, data)
# 把响应的json转换为字典
dic = json.loads(response.content.decode())

# 获取英文翻译结果
rs = dic['content'].get('out', None)
# 如果没有获取英文的翻译结果, 就获取中文的翻译结果
if not rs:
    rs = dic['content']['word_mean'][0]
# 输出最终结果
print(rs)
