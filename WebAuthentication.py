#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib2
import cookielib
import socket

localip = socket .gethostbyname(socket .gethostname() )
print localip
account = raw_input(u"账号\n")
password = raw_input(u"密码\n")
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2490.71 Safari/537.36',
           'Referer' : 'http://enet.10000.gd.cn:10001'}

loginoutdata = 'eduuser='+localip+'&edubas=113.98.13.29'
loginurl = "http://125.88.59.131:10001/login.do?edubas=113.98.13.29&eduuser="+localip+\
           "&userName1="+account+"&password1="+password
loginouturl = "http://enet.10000.gd.cn:10001/Logout.do"
#cookies
cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)
#end
get1 = raw_input(u"请输入y登陆，n注销登陆\n")
if get1 == 'y':
    request = urllib2.Request(loginurl, headers=headers)
    response = urllib2.urlopen(request)
    text = response.read().decode('utf-8')
    print(request)
    print(text)
if get1 == 'n':
    request = urllib2.Request(loginouturl,loginoutdata,headers)
    response = urllib2.urlopen(request)
    text = response.read().decode('utf-8')
    print(request)
    print(text)