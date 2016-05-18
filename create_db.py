# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 23:08:16 2015

@author: tete
"""
import sqlite3
conn = sqlite3.connect('FuBeacon.db')

conn.execute('''CREATE TABLE FBDEVDATA
        (NUMBER INT PRIMARY KEY  NOT NULL,
         ID CHAR(50)    NOT NULL,
         CORNAME CHAR(50)   NOT NULL,
         MESSAGE TEXT ,
         CATEGORY CHAR(10)   NOT NULL,
         PRETIME INT );''')


print '---------------------- Database created successful ----------------------\n'

# Inserted default value.
conn.execute("INSERT INTO FBDEVDATA(NUMBER,ID,CORNAME,MESSAGE,CATEGORY) \
            VALUES (1,'uuid_1major_1minor_1','肯德基','香辣鸡腿堡8.5折','FOOD')")
conn.commit()

conn.execute("INSERT INTO FBDEVDATA(NUMBER,ID,CORNAME,MESSAGE,CATEGORY) \
            VALUES (2,'uuid_1major_1minor_2','美美服装','新款服装上市。短裤，T恤。。。','CLOTH')")
conn.commit()

print 'Setting default value successful.'
conn.close()
