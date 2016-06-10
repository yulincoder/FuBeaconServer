# -*- coding: utf-8 -*-

from smtp import SMTPAlert
import threading
import socket
import json
import time

REMOTEHOST = ('127.0.0.1',8080)
BUFFSIZE = 1024
timeout = 4
#s.settimeout(timeout)
hoststate = None
print '------------------------------------------------------------'
print '--                         服务器监控                    --'
print '------------------------------------------------------------'


def loopmonitor():
	global REMOTEHOST,BUFFSIZE
	global hoststate
	while True:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

		time.sleep(5)
		try:	
			s.connect(REMOTEHOST)
		except Exception, e:
			if hoststate or hoststate is None :
				hoststate = False
				localtime = time.asctime( time.localtime(time.time()) )
				sender = SMTPAlert()
				msg = ('通知：1号服务器APP客户端连接异常' +"\n --  " + localtime)
				sender.send(msg)
				s.close()
				print '|    状态 : 异常    |    时间: %s    |' % localtime
		else:
			if hoststate is False or hoststate is None :
				hoststate = True
				localtime = time.asctime( time.localtime(time.time()) )
				sender = SMTPAlert()
				msg = ('通知：1号服务器APP客户端连接恢复' +"\n --  " + localtime)
				sender.send(msg)
				s.send('monitor')
				s.close()
				print '|    状态 : 正常    |    时间: %s    |' % localtime
		
if __name__ == '__main__':
	loopmonitor()

'''
while True:
    sock,addr = s.accept()
    
    t = threading.Thread(target=tcp_task,args=(sock,addr))
    t.start()
'''

'''
sender = SMTPAlert()
sender.send('Minotor create succfess!!')
'''