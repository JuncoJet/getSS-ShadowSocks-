#!/usr/bin/python
#coding=utf-8
import requests
from bs4 import BeautifulSoup
for i in range(140,250):
    url="http://free.818bbs.cn/index.php?main_page=domain&id=%d"%i
    r=requests.get(url)
    t=r.text
    #print t
    if t.find("vpn")<0 and t.find("dns")<0:
        try:
            s=BeautifulSoup(t,"html.parser")
            t=s.table.get_text()
            if t.find('http')<0 and t.find("DNS")<0:
                s=t.split('\n')
                print "%d."%i
                for x in s:
                    if x.find(u"请看")<0 and x.find(u'注意')<0 and len(x)>2:
                        #win平台可能需要转gbk
                        print x#.encode('gbk')
                print
        except Exception,e:
            e
