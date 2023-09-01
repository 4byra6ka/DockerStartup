import requests
from django.conf import settings


def tg_get_updates(offset=None):
    """Функция получения сообщения из телеграм бота"""
    params = {}
    if offset is not None:
        params = {'offset': offset}
    response = requests.get(f'https://api.telegram.org/bot{settings.TG_API_KEY}/getUpdates', params=params)
    return response.json()


def tg_send_message(chat_id, text):
    """Процедура отправки сообщения в телеграм"""
    params = {'chat_id': chat_id, 'text': text}
    requests.get(f'https://api.telegram.org/bot{settings.TG_API_KEY}/sendMessage', params=params)
