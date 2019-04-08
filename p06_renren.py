#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Xie1
# @Time: 19-4-7 19:12
# @File: p06_renren.py


import requests
import js2py

# 1. 获取requests中的session对象
session = requests.session()
# 登录手机端人人网
# 请求头
session.headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mo'
}

# 2. 使用session发送rKey获取登录需要信息
# 2.1 准备rkey请求的URL:
rkey_url = 'http://activity.renren.com/livecell/rKey'
# 2.2 使用session对象, 发送请求, 获取响应数据
response = session.get(rkey_url)
# 2.3 解析响应数据, 获取需要的数据
# 获取data中数据, 也就是js中n的值; `rkey`也在其中
n = response.json()['data']
print(n)

# 3. 使用js2py执行加密密码的js, 获取加密后的密码(难点)
# 3.1 定义生成加密密码的js 字符串
js = '''
     t.password = t.password.split("").reverse().join(""),
     setMaxDigits(130);
     var o = new RSAKeyPair(n.e,"",n.n)
     , r = encryptedString(o, t.password);
 '''

# 3.2 使用js2py获取js的执行环境
context = js2py.EvalJs()

# 3.3 使用js的执行环境加载或执行, js所依赖的js文件
context.execute(session.get(
    'http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/BigInt.js').content.decode())
context.execute(session.get(
    'http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/RSA.js').content.decode())
context.execute(session.get(
    'http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/Barrett.js').content.decode())

# 3.4 向js执行环境中,添加js中需要的数据
# 设置数据n
context.n = n
# 设置t.password
context.t = {
    'password': 'a123456'  # 准备要加密密码
}
# 3.5 执行js生成加密后的密码
context.execute(js)
# 3.6 获取加密后的密码
password = context.r
print(password)

# 4.  使用session对象发送登录请求, 登录人人网手机端.
# 4.1 准备登录请求的URL
login_url = 'http://activity.renren.com/livecell/ajax/clog'
# 4.2 准备登录请求的数据
data = {
    'phoneNum': '15565280933',  # 用户录入, 先写死
    'password': password,  # js对密码进行加密后的字符串
    'c1': '-100',  # 固定值, 直接写死
    'rKey': n['rkey'],  # rkey请求返回的值
}
# 4.3 使用session发送登录请求
response = session.post(login_url, data=data)

# 4.4 打印登录结果
print(response.content.decode())
