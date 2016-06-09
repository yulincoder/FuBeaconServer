# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 18:53:50 2016

@author: tete
"""

import sqlite3
import time

DB_FILE_PATH = 'FuBeacon.db'

TABLE_NAME = 'FBDEVDATA'



class BeaconDevAdapter:
    
    PATH = 'FuBeacon.db'
    SAVE_INDEX = {'number':0,'id':1,'cor_name':2,'message':4,'category':5,'prev_time':6}
    CATEGORY = ('FOOD','CLOTH','PARKING')
    STATE = {'1':'password error',
             '2':'id not match'}
   
    def __init__(self):
        self.connect_db()
        
        # A row information of FuBeacon from database.
        self.dev_info = self.get_dev_info()
    
    def get_msg_with_id(self,dev_id):
        if self.get_dev_info() is not None:
            if self.get_dev_info().__len__ != 0:
                for each in self.get_dev_info():
                    if dev_id == each[1]:
                        return each[2],each[3]
                        
        return None

    def get_category_with_id(self,dev_id):
        if self.get_dev_info() is not None:
            if self.get_dev_info().__len__ != 0:
                for each in self.get_dev_info():
                    if dev_id == each[1]:
                        return each[4]                     
        return None


    def get_hourvisit_with_id(self,dev_id):
        if self.get_dev_info() is not None:
            if self.get_dev_info().__len__ != 0:
                for each in self.get_dev_info():
                    if dev_id == each[1]:
                        return each[6]           
        return None

    def get_visit_with_id(self,dev_id):
        if self.get_dev_info() is not None:
            if self.get_dev_info().__len__ != 0:
                for each in self.get_dev_info():
                    if dev_id == each[1]:
                        return each[7]           
        return None


        
    def get_number_with_id(self,dev_id):
        if self.get_dev_info() is not None:
            if self.get_dev_info().__len__ != 0:
                for each in self.get_dev_info():
                    if dev_id == each[1]:
                        return each[0]
                        
        return None
        
    def id_in_database(self,dev_id):
        if self.get_dev_info() is not None:
            if self.get_dev_info().__len__ != 0:
                for each in self.get_dev_info():
                    if dev_id == each[1]:
                        return True
                        
        return False
        
    
    def set_rssi(self,dev_id,rssi):
        if type(rssi) == int:
            if self.id_in_database(dev_id):
                cu = self.conn.cursor()
                number = self.get_number_with_id(dev_id)
                data = (rssi,number)
                update_sql = "UPDATE FBDEVDATA SET RSSI=? WHERE NUMBER=?"
                cu.execute(update_sql,data)
                self.conn.commit()
                return True
        else:
            return False
        
    def get_rssi(self,dev_id):
        if self.get_dev_info() is not None:
            if self.get_dev_info().__len__ != 0:
                for each in self.get_dev_info():
                    if dev_id == each[1]:
                        return each[5]
    
#更新语句：update 表名 set 字段名=值 where 条件子句。如：update person set name=‘传智‘ where id=10       
    def update_msg_with_id(self,dev_id,msg):
        if self.id_in_database(dev_id):
            cu = self.conn.cursor()
            number = self.get_number_with_id(dev_id)
            data = (msg,number)
            update_sql = "UPDATE FBDEVDATA SET MESSAGE=? WHERE NUMBER=?"
            cu.execute(update_sql,data)
            self.conn.commit()
        else:
            return False
    
    
    def update_corname_with_id(self,dev_id,corname):
        if self.id_in_database(dev_id):
            cu = self.conn.cursor()
            number = self.get_number_with_id(dev_id)
            data = (corname,number)
            update_sql = "UPDATE FBDEVDATA SET CORNAME=? WHERE NUMBER=?"
            cu.execute(update_sql,data)
            self.conn.commit()
            #self.update(self.conn,update_sql,data)
        else:
            return False


    def update_category_with_id(self,dev_id,category):
        if category in BeaconDevAdapter.CATEGORY:
            if self.id_in_database(dev_id):
                cu = self.conn.cursor()
                number = self.get_number_with_id(dev_id)
                data = (category,number)
                update_sql = "UPDATE FBDEVDATA SET CATEGORY=? WHERE NUMBER=?"
                cu.execute(update_sql,data)
                self.conn.commit()



    def update_hourvisit_with_id(self,dev_id,time):
        if self.id_in_database(dev_id):
            cu = self.conn.cursor()
            number = self.get_number_with_id(dev_id)
            data = (time,number)
            update_sql = "UPDATE FBDEVDATA SET HOURVISIT=? WHERE NUMBER=?"
            cu.execute(update_sql,data)
            self.conn.commit()


    def update_visit_with_id(self,dev_id,time):
        if self.id_in_database(dev_id):
            cu = self.conn.cursor()
            number = self.get_number_with_id(dev_id)
            data = (time,number)
            update_sql = "UPDATE FBDEVDATA SET VISIT=? WHERE NUMBER=?"
            cu.execute(update_sql,data)
            self.conn.commit()


               
    def connect_db(self):  
        self.conn = sqlite3.connect(BeaconDevAdapter.PATH)
        
    def close_db(self):
        self.conn.close()
        
    def get_dev_info(self):
        # Obtain device's id in database with uuid,major and minor.
        cur = self.conn.cursor()
        cur = self.conn.execute("SELECT NUMBER,ID,CORNAME,MESSAGE,CATEGORY,RSSI,HOURVISIT,VISIT from FBDEVDATA")
        all_dev = cur.fetchall()
        
        rows = []
        for row in all_dev:
            if row[2] is not None:
                rows.append(row)
        if rows.__len__ is not 0:
            return rows
        else:                
            return None
# Codes following can be run only one.
# Created database.
            
if __name__ == '__main__':
    
    test = BeaconDevAdapter()

    dev_id = u'uuid_1major_1minor_1'
    #test.set_time(dev_id,-44)  
    print test.get_rssi(dev_id)

    if test.id_in_database(dev_id):
        print test.get_number_with_id(dev_id)
        print test.get_msg_with_id(dev_id)[0],test.get_msg_with_id(dev_id)[1]
        print 'cate:',test.get_category_with_id(dev_id)
        test.update_hourvisit_with_id(dev_id,10)
        print 'hourvisit:',test.get_hourvisit_with_id(dev_id)
        test.update_visit_with_id(dev_id,50)
        print 'visit:',test.get_visit_with_id(dev_id)
    else:
        print 'Not exist'

    dev_id = u'uuid_1major_1minor_2'
    #test.set_rssi(dev_id,-90)   
    print test.get_rssi(dev_id),type(test.get_rssi(dev_id))
    #test.set_time(dev_id,int(time.time()))
    #test.update_msg_with_id(dev_id,u'成功啦')
    #test.update_corname_with_id(dev_id,u'陕西省榆林市')
    if test.id_in_database(dev_id):
        print test.get_number_with_id(dev_id),type(test.get_number_with_id(dev_id))
        print test.get_msg_with_id(dev_id)[0],test.get_msg_with_id(dev_id)[1]

    else:
        print 'Not exist'
    



'''
conn = sqlite3.connect('FuBeacon.db')
cursor = conn.cursor()
cursor = conn.execute("SELECT ID,UUID,MAJOR,MINOR,MESSAGE,CATEGORY,PASSWORD from FBDEVDATA")
'''
#uuid = cursor.fetchone()[0]
#conn.close()  
#print cursor.fetchall()
'''
for row in cursor.fetchall():
    for each in row:
        print each

conn.close()  
'''     
