# -*- coding: utf-8 -*-
"""
Created on Tue May 17 15:00:25 2016

@author: tete
"""
from flask.ext.wtf import Form
#from wtforms import StringField,SubmitField,PasswordField
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import Required

class DevNameForm(Form):
    #dev_id = StringField(u'设置设备ID',validators=[Required()])

    dev_id = SelectField('设备ID', choices=[('uuid_1major_1minor_1','uuid_1major_1minor_1'), ('uuid_1major_1minor_2','uuid_1major_1minor_2')])
#    major = StringField(u'设备 Major',validators=[Required()])
#    minor = StringField(u'设备 Minor',validators=[Required()])
#    password = PasswordField(u'设备密码',validators=[Required()])
    cor_name = StringField(u'设置机构名称',validators=[Required()])
    message = StringField(u'设置推送消息',validators=[Required()])
    
    #category = StringField(u'消息类别',validators=[Required()])
    category = SelectField('消息类别', choices=[('FOOD','餐饮'), ('CLOTH','服装')])
    proxi_state = SelectField('距离', choices=[(-40,'近'), (-60, '中'),(-80, '远')])
    submit = SubmitField('提交')
