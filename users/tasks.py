from celery import shared_task

from users.models import User
from users.services import tg_get_updates, tg_send_message


@shared_task
def telegram_bot_updates():
    """Периодическая задача(каждую минуту) опрос телеграм бота на получения команды '/start' и активация пользователя"""
    tg_data = tg_get_updates()
    users = User.objects.filter(is_active=False)
    if tg_data['ok'] and tg_data['result'] != []:
        for message in tg_data['result']:
            if message['message']['text'] == "/start":
                for user_one in users:
                    if user_one.username.lower() == message['message']['from']['username'].lower():
                        password = User.objects.make_random_password()
                        user_one.set_password(password)
                        user_one.tg_user_id = message['message']['from']['id']
                        user_one.first_name = message['message']['from']['first_name']
                        user_one.last_name = message['message']['from']['last_name']
                        user_one.is_active = True
                        user_one.save()
                        tg_get_updates(message['update_id'])
                        text = f'Ваша учетная запись активирована. Пароль для входа:\n{password}'
                        tg_send_message(message['message']['from']['id'], text)
            tg_get_updates(message['update_id'])
