# -*- coding: utf-8 -*-
"""
Created on Wed May 18 01:25:37 2016

@author: tete
"""

import threading
import socket
import json
import time
from database import BeaconDevAdapter

ADDR = '0.0.0.0'
PORT = 8080
BUFFSIZE = 1024

#REMOTEHOST = ('123.206.81.181',10002)
#REMOTEHOST = ('121.42.199.230',10001)
REMOTEHOST = ('127.0.0.1',10002)
BUFFSIZE = 1024


dev_pre_time = {'uuid_1major_1minor_1':0,'uuid_1major_1minor_2':0}

def tcp_task(sock,addr):
    global REMOTEHOST,BUFFSIZE
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    json_data = sock.recv(BUFFSIZE)
    try:
        req_data = json.loads(json_data)
        dev_id = req_data['ID']
        rssi = int(req_data['RSSI'])
        adapter = BeaconDevAdapter()
        time_now = int(time.time())
    
        corname = adapter.get_msg_with_id(dev_id)[0]
        msg = adapter.get_msg_with_id(dev_id)[1]
    
        pre_time = dev_pre_time[dev_id]
        #pre_time = adapter.get_prev_time(dev_id) # It can come up a database locked error.
        #adapter.set_time(dev_id,time_now) 
        sett_rssi = adapter.get_rssi(dev_id)
        print '设置距离 --' + str(sett_rssi) +'--'+ str(type(sett_rssi))+'--'
        
        if rssi > sett_rssi:
            dev_pre_time[dev_id] = time_now # Update the time.
            if time_now-pre_time > 3:
                resp_data = json.dumps({'corname':corname,'fuda':msg})
                
                try:    
                    s.connect(REMOTEHOST)
                    hourvisit = adapter.get_hourvisit_with_id(dev_id) + 1
                    adapter.update_hourvisit_with_id(dev_id,hourvisit)
                    visit = adapter.get_visit_with_id(dev_id) + 1
                    adapter.update_visit_with_id(dev_id,visit)
                    s.send(json.dumps({"id":dev_id,"visit":visit,"hourvisit":hourvisit}))
                except:
                    print 'Remote host error!'
            else:
                resp_data = json.dumps({'corname':'null','fuda':'null'})
        else:
            resp_data = json.dumps({'corname':'null','fuda':'null'})
        print '实时距离 --' + str(rssi)+'--' + str(type(rssi)) + '--'
        adapter.close_db()
    except:
        resp_data = json.dumps({'corname':'null','fuda':'null'})
    finally:  
        sock.send(resp_data)
        sock.close()


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((ADDR,PORT))
s.listen(5)
print 'Waiting ...'

while True:
    sock,addr = s.accept()
    
    t = threading.Thread(target=tcp_task,args=(sock,addr))
    t.start()
