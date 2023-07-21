from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

app = Celery('django_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    # Executes every 5 seconds with crontab
    'add-every-5-seconds': {
        'task': 'stock_price.tasks.add',
        'schedule': 5,
        'args': (16, 16)
    },
}


app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)