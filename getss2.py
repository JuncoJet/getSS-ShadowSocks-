#!/usr/bin/python
#coding=utf-8
import requests
from bs4 import BeautifulSoup
for i in range(200):
    url="http://818bbs.cn/thread-%d-1-1.html"%i
    r=requests.get(url)
    t=r.text
    #print t
    try:
        s=BeautifulSoup(t,"html.parser")
        t=s.find('td',class_='t_f').get_text()
        #print t
        if t.find(u'密码')>0 and t.find(u'加密')>0:
            print "%d."%i,
            print t
            print
    except Exception,e:
        e
