# -*- coding: utf-8 -*-

import os

print '----  dictory ----'
os.system('pwd')

print '----  execute git add  -----'
files = 	['BeaconServer.py','config.py','create_db.py','database.py','FuBeacon.db',
	'monitor.py','git.py','README.md','run.py','smtp.py','syn.py']

time = 0
for file in files:
	time += 1
	print 'git add %s files.' %  str(time)
	os.system('git add ' + file)

#os.system('cd /app')
#print '----    dictory  ----'
print  '/app' 
files = ['database.py','forms.py','FuBeacon.db','__init__.py','views.py']
time = 0
for file in files:
	time += 1
	print 'git add %s files.' %  str(time)
	os.system('git add ' + 'app/' + file)

print '----    dictory  ----'
print  '/app' + '/templates'
files = ['about.html','base.html','index.html','list.html','setting.html']
time = 0
for file in files:
	time += 1
	print 'git add %s files.' %  str(time)
	os.system('git add ' + 'app/templates/' + file)
