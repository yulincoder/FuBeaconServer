# -*- coding: utf-8 -*-
"""
Created on Tue May 17 14:42:30 2016

@author: tete
"""

from flask import render_template,url_for,redirect,request
from app import app
from .forms import DevNameForm
from .database import BeaconDevAdapter
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():
    return render_template('index.html',title='FuBeacon')
    
    
@app.route('/life',methods=['GET','POST'])
def mylife():
    return render_template('index.html',title='FuBeacon',change='life')


def get_devinfo(number):
    CATEGORY = {'FOOD':'餐饮','CLOTH':'服装','PARKING':'停车'}
    adapter = BeaconDevAdapter()
    if number == 1:
        devtemp = {}
        dev_id = 'uuid_1major_1minor_1'
        devtemp['id'] = dev_id
        devtemp['corname'] = adapter.get_msg_with_id(dev_id)[0]
        devtemp['message'] = adapter.get_msg_with_id(dev_id)[1]
        
        if adapter.get_category_with_id(dev_id) in CATEGORY:
            devtemp['category'] = CATEGORY[adapter.get_category_with_id(dev_id)]
            
        if   adapter.get_rssi(dev_id)  >= -40:
            devtemp['distance'] = '近'
        elif adapter.get_rssi(dev_id) < -40 and adapter.get_rssi(dev_id) >= -60:
            devtemp['distance'] = '中'
        elif adapter.get_rssi(dev_id) < -60 and adapter.get_rssi(dev_id) >= -80:
            devtemp['distance'] = '远'
        else:
            devtemp['distance'] = '未知'

        devtemp['hourvisit'] = adapter.get_hourvisit_with_id(dev_id)
        devtemp['visit'] = adapter.get_visit_with_id(dev_id)
        return devtemp
    elif number == 2:
        devtemp = {}
        dev_id = 'uuid_1major_1minor_2'
        devtemp['id'] = dev_id
        devtemp['corname'] = adapter.get_msg_with_id(dev_id)[0]
        devtemp['message'] = adapter.get_msg_with_id(dev_id)[1]
      
        if adapter.get_category_with_id(dev_id) in CATEGORY:
            devtemp['category'] = CATEGORY[adapter.get_category_with_id(dev_id)]
         
        if   adapter.get_rssi(dev_id)  >= -40:
            devtemp['distance'] = '近'
        elif adapter.get_rssi(dev_id) < -40 and adapter.get_rssi(dev_id) >= -60:
            devtemp['distance'] = '中'
        elif adapter.get_rssi(dev_id) < -60 and adapter.get_rssi(dev_id) >= -80:
            devtemp['distance'] = '远'
        else:
            devtemp['distance'] = '未知'

        devtemp['hourvisit'] = adapter.get_hourvisit_with_id(dev_id)
        devtemp['visit'] = adapter.get_visit_with_id(dev_id)
        return devtemp


@app.route('/list')
def devicelist():
    devinfo = []
    devinfo.append(get_devinfo(1))
    devinfo.append(get_devinfo(2))

    return render_template('list.html',devinfo=devinfo)

    
@app.route('/setting',methods=['GET','POST'])
def dev_setting():
    form = DevNameForm()
    adapter = BeaconDevAdapter()
    
    corname = ''
    msg = ''
    dev_id = ''    
    test = 'xxx'
    print 'Into setting...'

    if request.method == 'POST':
        
        print '一次请求。。。'
        corname = form.cor_name.data
        msg = form.message.data
        dev_id = form.dev_id.data
        #print int(form.proxi_state.data),type(int(form.proxi_state.data))
        
        if len(dev_id) != 0:
            adapter.set_rssi(dev_id.decode(),int(form.proxi_state.data))		
        print '依次是： ',corname,msg,dev_id
        #adapter.update_corname_with_id(dev_id,u'及八宝')
        if len(corname) != 0 and len(dev_id) != 0:
            adapter.update_corname_with_id(dev_id.decode().encode('utf-8'),corname.decode())
        
        if len(msg) != 0 and len(dev_id) != 0:
            adapter.update_msg_with_id(dev_id.decode().encode('utf-8'),msg.decode())
        test = '有'

        # return to list page.
        devinfo = []
        devinfo.append(get_devinfo(1))
        devinfo.append(get_devinfo(2))
        return render_template('list.html',devinfo=devinfo)
        
    return render_template('setting.html',form=form,test = test)


    
@app.route('/about')
def about():
    return render_template('about.html')
