#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import requests
import sys
from pytesser import image_to_string
from PIL import Image
import time


def getverify1():
    headers_1 = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'Cookie':'loginInfo=TrZ8QGOkMeDViIlqMt8yaddowAuqeCbj+xWgsjQMFHHolBC5kzI+KONdjuAU/ARb; md=341C882D880E8E665AAC53AC1F31B570B6817396',
        'Host':'125.88.59.131:10001',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    rep = {'O': '0',
           'I': '1',
           'L': '1',
           'Z': '2',
           'S': '8'
           }
    r = requests.get('http://125.88.59.131:10001/login.jsp?wlanuserip=10.101.187.210&wlanacip=113.98.13.29', headers=headers_1)
    codecookies = r.cookies['JSESSIONID']
    headers_2 = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':'loginInfo=TrZ8QGOkMeDViIlqMt8yaddowAuqeCbj+xWgsjQMFHHolBC5kzI+KONdjuAU/ARb; md=341C882D880E8E665AAC53AC1F31B570B6817396 ;JSESSIONID='+codecookies+'; signature=D0AB8BE4413F52D798C67E23DC8E8A78',
        'Host':'125.88.59.131:10001',
        'Referer':'http://125.88.59.131:10001/login.jsp?wlanuserip=10.101.187.210&wlanacip=113.98.13.29',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    timestamp = str(int(time.time()))
    r = requests.get('http://125.88.59.131:10001/common/image.jsp?time='+timestamp, stream=True, headers=headers_2)

    # r = requests.get('http://125.88.59.131:10001/common/image.jsp?time=1463198266151', stream=True, headers=headers)
    try:
        with open('image.jpg', 'wb') as f:
            f.write(r.content)
            f.close()
    except IOError:
        print("IO Error\n")
    im = Image.open('image.jpg')
    imgry = im.convert('L')
    out = imgry.point(table, '1')
    text = image_to_string(out)
    text = text.strip()
    text = text.upper()

    for r in rep:
        text = text.replace(r, rep[r])

    #out.save(text+'.jpg')
    print text
    return text, codecookies


def logincampus():
    request_url = 'http://125.88.59.131:10001/login.do'
    # sys.path.append('tessdata/')
    # import campuscode
    rand, codecookies = getverify1()
    headers_3 = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Content-Length':'97',
    'Content-Type':'application/x-www-form-urlencoded',
    'cookie':'loginInfo=TrZ8QGOkMeDViIlqMt8yaddowAuqeCbj+xWgsjQMFHHolBC5kzI+KONdjuAU/ARb;md=341C882D880E8E665AAC53AC1F31B570B6817396;signature=D0AB8BE4413F52D798C67E23DC8E8A78;JSESSIONID='+codecookies,
    'Host':'125.88.59.131:10001',
    'Origin':'http://125.88.59.131:10001',
    'Referer':'http://125.88.59.131:10001/login.jsp?wlanuserip=10.101.187.210&wlanacip=113.98.13.29',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                 ' Chrome/50.0.2661.102 Safari/537.36'}

    payload = {'userName1': 'your username', 'password1': 'your password', 'rand': rand, 'eduuser': '10.101.187.210',
               'edubas': '113.98.13.29', 'checkbox': 'on'}
    r = requests.post(request_url, data=payload, headers=headers_3)
    print r.text
if __name__ == "__main__":
    logincampus()


