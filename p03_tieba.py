#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Xie1
# @Time: 19-4-6 20:46
# @File: p03_tieba.py

import requests

# https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&ie=utf-8&pn=50

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

url_prefix = 'https://tieba.baidu.com/f?kw=李毅&pn='
for i in range(1, 4):
    pn = (i-1)*50
    url = url_prefix + str(pn)


    response = requests.get(url=url, headers=headers)
    with open('html/p03_'+str(i)+'.html', 'wb')as f:
        f.write(response.content)
