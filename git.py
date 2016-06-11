# -*- coding: utf-8 -*-

import os

print '----  dictory ----'
os.system('pwd')

print '----  execute git add  -----'
files = 	['BeaconServer.py','config.py','create_db.py','database.py','FuBeacon.db',
	'monitor.py','git.py','README.md','run.py','smtp.py','syn.py']

for file in files:
	print 'git add %s .' %  file
	os.system('git add ' + file)
print 'git add %s files.' %  str(len(files))

#os.system('cd /app')
#print '----    dictory  ----'
print  '/app' 
files = ['database.py','forms.py','FuBeacon.db','__init__.py','views.py']

for file in files:
	print 'git add %s .' %  file
	os.system('git add ' + 'app/' + file)
print 'git add %s files.' %  str(len(files))

print '----    dictory  ----'
print  '/app' + '/templates'
files = ['about.html','base.html','index.html','list.html','setting.html']
time = 0
for file in files:
	print 'git add %s .' %  file
	os.system('git add ' + 'app/templates/' + file)
print 'git add %s files.' %  str(len(files))
