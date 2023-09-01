import json
from datetime import datetime, date

from django_celery_beat.models import PeriodicTask, IntervalSchedule


def create_periodic_task(frequency, pk, time):
    """Создание периодической задачи"""
    schedule, created = IntervalSchedule.objects.get_or_create(
         every=frequency,
         period=IntervalSchedule.DAYS,
     )
    return PeriodicTask.objects.create(
        interval=schedule,
        name=f'{pk}',
        task='habits.tasks.habits_send_telegram',
        start_time=datetime.combine(date.today(), time),
        args=json.dumps({}),
        kwargs=json.dumps({'pk': pk})
     )
