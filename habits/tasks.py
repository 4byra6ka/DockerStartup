from celery import shared_task

from habits.models import Habit
from users.services import tg_send_message


@shared_task
def habits_send_telegram(**kwargs):
    """Отправка уведомления привычки"""
    habit = Habit.objects.get(pk=kwargs['pk'])
    tg_send_message(habit.owner.tg_user_id, str(habit))
