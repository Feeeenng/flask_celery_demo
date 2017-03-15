# -*- coding: UTF-8 -*-
'''
@author: 'FenG_Vnc'
@date: 2017-03-15 12:07
@file: config.py
'''
from __future__ import unicode_literals

from celery.schedules import timedelta

class Config:
    DEBUG = True
#   celery配置
    CELERY_BROKER_URL = 'redis://192.168.0.203:6379/2'   #redis 服务器配置
    CELERY_RESULT_BACKEND = 'redis://192.168.0.203:6379/2'  #redis 服务器配置
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_ACCEPT_CONTENT = ['application/json']
#   数据获取、分析周期设置
    CELERYBEAT_SCHEDULE = {
        'job1': {
            'task': 'app.tasks.job1',
            'schedule': timedelta(seconds=10),
            'args': (),
            }
    }
#   celery时区
    CELERY_TIMEZONE = 'Asia/Shanghai'
    @staticmethod
    def init_app(app):
        pass
class DevelopmentConfig(Config):
    DEBUG = True
    #@classmethod
    #def init_app(cls, app):
     #   config.init_app(app)
config = {
    'development': DevelopmentConfig,
   # 'testing': TestingConfig,
   # 'production': ProductionConfig,
  #  'heroku': HerokuConfig,
  #  'unix': UnixConfig,

    'default': DevelopmentConfig
}
