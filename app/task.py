# -*- coding: UTF-8 -*-
'''
@author: 'FenG_Vnc'
@date: 2017-03-15 12:08
@file: task.py
'''
from __future__ import unicode_literals



from app import celery



@celery.task
def job1():

    return 'hello celery'