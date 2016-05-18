# -*- coding: utf-8 -*-
"""
Created on Tue May 17 14:42:30 2016

@author: tete
"""

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string.'
#app.config.from_object('config')

from app import views
