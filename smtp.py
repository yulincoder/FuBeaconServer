# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

class SMTPAlert:
	def __init__(self):
		self.from_addr = 'okfanjin@163.com'
		self.password = 'tete123456'
		self.to_addr = ['784773435@qq.com']
		self.smtp_server = 'smtp.163.com'
		self.subject = '服务器监控消息'

	def _format_addr(self,s):
    		name, addr = parseaddr(s)
    		return formataddr(( \
        			Header(name, 'utf-8').encode(), \
        			addr.encode('utf-8') if isinstance(addr, unicode) else addr))

    	def send(self,content):
    		msg = MIMEText(content, 'plain', 'utf-8')
		msg['From'] = self._format_addr(u'FuBeacon Inc <%s>' % self.from_addr)
		msg['To'] = self._format_addr(u'管理员 <%s>' % self.to_addr)
		msg['Subject'] = Header(self.subject, 'utf-8').encode()

		server = smtplib.SMTP(self.smtp_server, 25)
		#server.set_debuglevel(1) #Print inform of debug.
		server.set_debuglevel(0)
		server.login(self.from_addr, self.password)
		server.sendmail(self.from_addr, self.to_addr, msg.as_string())
		server.quit()
		return True

	def set_recver(self,recver):
		# recver is a list.
		self.to_addr = recver

	def set_emailtitle(self,subject):
		self.subject = subject

if __name__ == '__main__':
	sender = SMTPAlert()
	sender.send('from SMTEALERT class ...')
'''
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = 'okfanjin@163.com'
password = 'tete123456'
to_addr = ['784773435@qq.com','1055382519@qq.com']
smtp_server = 'smtp.163.com'

msg = MIMEText('发生大问题啦啦啦..', 'plain', 'utf-8')
msg['From'] = _format_addr(u'FuBeacon Inc <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'服务器监控消息', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()
print 'over ..'
'''