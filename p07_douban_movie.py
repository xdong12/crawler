#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Xie1
# @Time: 19-4-8 10:04
# @File: p07_douban_movie.py


import requests
import json


class DoubanMovie(object):

    def __init__(self):
        #  2.1. start使用占位符进行占位; start={}
        # 准备URL
        self.url = 'https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?start={}&count=18&loc_id=108288'
        # 准备请求头
        self. headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
            'Referer': 'https://m.douban.com/movie/nowintheater?loc_id=108288'
        }

    def get_content_from_url(self, url):
        """发送请求, 获取响应"""
        response = requests.get(url, headers=self.headers)
        # 返回响应内容
        return response.content.decode()

    def get_data_from_content(self, content):
        """根据响应内容, 提取电影信息"""
        # json => python
        rs = json.loads(content)
        data = rs['subject_collection_items']
        return data

    def save_data(self, data):
        """保存数据"""
        # 以每一行是一个json格式的数据来写, 这种文件类型为jsonlines
        with open('json/p07_.jsonlines', 'a', encoding='utf8') as f:
            for movie in data:
                json.dump(movie, f, ensure_ascii=False)
                f.write('\n')

    def run(self):

        # 2.2. 定义start的变量, 用于记录偏移量, 初始值为0
        start = 0
        # 2.3. 使用循环不断的发送请求, 每次start递增18
        while True:

            # 1. 准备URL和请求头
            url = self.url.format(start)
            # 2. 发送请求, 获取响应数据
            content = self.get_content_from_url(url)
            # 3. 提取电影信息
            data = self.get_data_from_content(content)
            # 4. 保存电影信息(以jsonlines, 写入到文件中)
            self.save_data(data)

            # 2.4. 如果响应电影条数不足18条件了, 结束循环
            if len(data) < 18:
                break
            # 2.3.2 每次start递增18
            start += 18




if __name__ == '__main__':
    dbm = DoubanMovie()
    dbm.run()
