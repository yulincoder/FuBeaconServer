# -*- coding: utf-8 -*-

import threading
import socket
import json
import time
from database import BeaconDevAdapter

ADDR = '0.0.0.0'
PORT = 10001
BUFFSIZE = 1024

def tcp_task(sock,addr):
    json_data = sock.recv(BUFFSIZE)
    adapter = BeaconDevAdapter()
    try:
        syndata = json.loads(json_data)
        #fromat of syndata is {'id':'xx','corname':'xx','msg':'xx','category':'xx','rssi':xx,'hourvisit':xx,'visit':xx}
        if 'id' in syndata:
            adapter.set_rssi(syndata['id'],syndata['rssi'])
            if  syndata['corname'] != 'null':
                adapter.update_corname_with_id(syndata['id'],syndata['corname'])
                print 'corname:',syndata['corname']
            if  syndata['msg'] != 'null':
                adapter.update_msg_with_id(syndata['id'],syndata['msg'])
                print 'msg:',syndata['msg']
            adapter.update_category_with_id(syndata['id'],syndata['category']);print 'syn success.'
            #adapter.update_hourvisit_with_id(syndata['id'],syndata['hourvisit'])
            #adapter.update_visit_with_id(syndata['id'],syndata['visit'])
        else:
            print 'syndata format error!.'
                
    except:
        print 'syndata error!'
    finally:
        sock.close()



s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((ADDR,PORT))
s.listen(5)
print 'Database syn listen : %s ...' % str(PORT) 

while True:
    sock,addr = s.accept()
    
    t = threading.Thread(target=tcp_task,args=(sock,addr))
    t.start()