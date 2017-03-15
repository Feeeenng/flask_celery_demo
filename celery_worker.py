# -*- coding: UTF-8 -*-
'''
@author: 'FenG_Vnc'
@date: 2017-03-15 12:08
@file: celery_worker.py
'''
from __future__ import unicode_literals


from app import create_app
from app.tasks import  celery


app = create_app('default')
app.app_context().push()

