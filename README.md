
# flask 跟 celery 在实际项目中的用法. 需要安装 flask,redis,celery

# windows 使用方法 需要开两个cmd窗口进入项目目录然后分别输入:
```
celery beat -A celery_worker.celery -l info
celery work -A celery_worker.celery -l info
```

# Liunx 也是一样

