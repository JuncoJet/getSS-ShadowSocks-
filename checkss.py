#!/usr/bin/python
#coding=utf-8
import socket,os,timeit
import json,copy
def check():
    global server,port
    socket.setdefaulttimeout(timeout)
    ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ss.connect((server,port))
    ss.send('HELLO')
timeout=5#设置超时时间
f=open("gui-config.json")#这里根据实际文件
txt=f.read()
j=json.loads(txt)
o=copy.deepcopy(j)
o['configs']=[]
for s in j['configs']:
    server=s['server']
    port=s['server_port']
    print "%s:%s"%(server,port),
    try:
        t=timeit.Timer("check()","from __main__ import check")
        print "%fs OK."%t.timeit(1)
        o['configs'].append({"server":server,
                           "server_port":port,
                           "password":s['password'],
                           "method":s['method'],
                           "remarks":''
                           })
    except Exception,e:
        print e
print
print json.dumps(o)
