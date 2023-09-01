from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Установка переменной окружения для настроек проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Создание экземпляра объекта Celery
app = Celery('config')

# Загрузка настроек из файла Django
app.config_from_object('django.conf:settings', namespace='CELERY')
#
# app.conf.beat_schedule = {
#     'TelegramBotUpdates': {
#         'task': 'users.tasks.telegram_bot_updates',
#         'schedule': 20.0,
#         'args': (16, 16)
#     },
# }
# app.conf.timezone = 'UTC'

# Автоматическое обнаружение и регистрация задач из файлов tasks.py в приложениях Django
app.autodiscover_tasks()
