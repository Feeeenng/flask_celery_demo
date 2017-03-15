# -*- coding: UTF-8 -*-
'''
@author: 'FenG_Vnc'
@date: 2017-03-15 12:07
@file: __init__.py.py
'''
from __future__ import unicode_literals
from flask import Flask
from config import config
from celery import Celery, platforms


celery = Celery(__name__, broker=config['development'].CELERY_BROKER_URL)


# 程序初始化
def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)


    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    platforms.C_FORCE_ROOT = True  # root用户启动

    return app