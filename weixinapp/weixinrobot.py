#!/usr/bin/python3
# -*- coding: utf-8 -*-

from werobot import WeRoBot

import re

import json
import requests
import time
import random
import string
import hashlib


# 微信公众号中，设置url 和 token 既可以处理 对话框消息
myrobot = WeRoBot(token='wx_test_token')

# 操作client,可以生成自定义菜单
myrobot.config["APP_ID"] = "wx003a117b3a52c2b5"
myrobot.config["APP_SECRET"] = "6995a83c37a7300ec67435974f6eb532"



"""
JS-SDK的页面必须先注入配置信息，否则将无法调用（同一个url仅需调用一次)
通过config接口注入权限验证配置
wx.config({
    debug: true, // 开启调试模式,调用的所有api的返回值会在客户端alert出来，若要查看传入的参数，可以在pc端打开，参数信息会通过log打出，仅在pc端时才会打印。
    appId: '', // 必填，公众号的唯一标识
    timestamp: , // 必填，生成签名的时间戳
    nonceStr: '', // 必填，生成签名的随机串
    signature: '',// 必填，签名
    jsApiList: [] // 必填，需要使用的JS接口列表
});
######## 微信 JS SDK 使用前需要签名
#    1、使用 appid 和 appsecrect 获取 access_token
#    2、使用 access_token 换取 js_ticket
#    3、使用 js_ticket, url 和一些变量来生成 signature
#########

签名生成规则如下：
 参与签名的字段包括
 noncestr（随机字符串）, 
 有效的jsapi_ticket, 
 timestamp（时间戳）, 
 url（当前网页的URL，不包含#及其后面部分） 。
 对所有待签名参数按照字段名的ASCII 码从小到大排序（字典序）后，
 使用URL键值对的格式（即key1=value1&key2=value2…）拼接成字符串string1。
 这里需要注意的是所有参数名均为小写字符。
 对string1作sha1加密，字段名和字段值都采用原始值，不进行URL 转义。
 即signature=sha1(string1)。 
"""
class JsApiTicketClient(object):
    def __init__(self, werobot_client):
        """
        根据werobot_client 初始化
        _JsAPITicket 为根据client的access token 生成的 js api ticket
        ticket_expires_at 为到期时间，= 获取时间 + 有效期
        """
        self.wrclient = werobot_client
        self._JsAPITicket = None
        self.ticket_expires_at = None

    def grant_JsAPITicket(self):
        """
        获取jsapi_tocket。
        :return: 返回的 JSON 数据包
        """
        _JSAPI_URL = r"https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token={0}&type=jsapi"
        _access_token = self.wrclient.get_access_token()
        _URL=_JSAPI_URL.format(_access_token)

        ret = requests.get(_URL)
        rjson = json.loads(ret.text)
        return rjson

    def getStrJsAPITicket(self):
        """
        判断现有的_ JsAPITicket 是否过期。
        用户需要多进程或者多机部署可以手动重写这个函数
        来自定义_JsAPITicket的存储，刷新策略。
        :return: 返回token
        """
        if self._JsAPITicket:
            now = time.time()
            if self.ticket_expires_at - now > 60:
                return self._JsAPITicket
        json = self.grant_JsAPITicket()
        self._JsAPITicket = json["ticket"]
        self.ticket_expires_at = int(time.time()) + json["expires_in"]
        return self._JsAPITicket

    def __create_nonce_str(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))

    def __create_timestamp(self):
        return int(time.time())

    def getconfig_sign_url(self,url):
        ret = {
            'nonceStr': self.__create_nonce_str(),
            'jsapi_ticket': self.getStrJsAPITicket(),
            'timestamp': self.__create_timestamp(),
            'url': url
        }
        string1 = '&'.join(['%s=%s' % (key.lower(), ret[key]) for key in sorted(ret)])
        # print(string1)
        hashstring = string1.encode('utf8')
        # print(hashstring)
        ret['signature'] = hashlib.sha1(hashstring).hexdigest()
        # print(ret['signature'])
        return ret

client = myrobot.client
myjsticketclient = JsApiTicketClient(client)

client.create_menu({
    "button":[
        {
            "type":"click",
            "name":"今日歌曲",
            "key":"music"
        },
        {
            "type":"view",
            "name":"Baidu搜索",
            "url":"http://www.baidu.com/"
        },
        {
            "name":"菜单",
            "sub_button":[
                {
                    "type":"click",
                    "name":"歌手简介",
                    "key":"V1001_TODAY_SINGER"

                },
                {
                    "type":"view",
                    "name":"HomePage",
                    "url":"http://59.110.152.204"

                },
                {
                    "type":"view",
                    "name":"微信jsSDK",
                    "url":"http://59.110.152.204/wx/demo"

                },
                {
                    "type":"view",
                    "name":"html5_GPS",
                    "url":"http://39.106.202.241:8888/h5gps.html"
                },
                {
                    "type":"view",
                    "name":"其他jsSDK",
                    "url":"http://39.106.202.241:8888/index.html"
                }

            ]
        }
    ]})


# @robot.handler ，类似 if elif ，以文件中顺序逐步判断，先return 即处理
#@myrobot.handler
#def hello(message):
#    return 'Hello World!'
@myrobot.subscribe
def subscribe(message):
    return "欢迎关注！发送a、包含bb、config、包含c或正文d、其他；图片。"

# @robot.image 修饰的 Handler 只处理图片消息
@myrobot.image
def img(message):
    return message.img

@myrobot.filter(re.compile(".*?配置.*?"), re.compile(".*?config.*?"))
def textconfig():
    _s_access_token = client.get_access_token()
    _s_jsapiticket = myjsticketclient.getStrJsAPITicket()
    _j_config = myjsticketclient.getconfig_sign_url(r'http://39.106.202.241:8888/index.html')
    _s_j_config = json.dumps(_j_config)
    return "access_token:: "+ _s_access_token +"___" + "jsapi_ticket:: "+ _s_jsapiticket +"___" + "config:: " + _s_j_config

@myrobot.filter(re.compile(".*?bb.*?"))
def b():
    return "正文中含有 bb "

@myrobot.filter(re.compile(".*?c.*?"), "d")
def cd():
    return "正文中含有 c ，或者正文为 d"

@myrobot.text
def textecho(message,session):
    if message.content == "a":
        count = session.get("count", 0) + 1
        session["count"] = count
        return "您好! 您发了 %s 次‘a’消息给我" % count
    else:
        return message.content
    

@myrobot.key_click("music")
def music(message):
    return '你点击了“今日歌曲”按钮'

@myrobot.click
def abort(message):
    if message.key == "V1001_TODAY_SINGER":
        return '您点击了"歌手"菜单'


def get_sign_config(surl):
    signjson={
        'app_id': myrobot.config["APP_ID"],
        'access_token': client.get_access_token(),
        'jsapi_ticket': myjsticketclient.getStrJsAPITicket(),
        'js_config': myjsticketclient.getconfig_sign_url(surl)
    }
    return signjson

# 让服务器监听在 0.0.0.0:80
# myrobot.config['HOST'] = '0.0.0.0'
# myrobot.config['PORT'] = 80
# myrobot.run()
