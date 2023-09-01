from django.db import models
from django.utils import timezone
from django_celery_beat.models import PeriodicTask

from users.models import User, NULLABLE


class Habit(models.Model):
    """Модель привычки"""
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Владелец привычек", **NULLABLE)
    place = models.CharField(max_length=150, verbose_name="Место выполнения привычки")
    time = models.TimeField(default=timezone.now, verbose_name="Время выполнения привычки")
    action = models.CharField(max_length=150, null=False, blank=False, verbose_name="Действие привычки")
    is_pleasant = models.BooleanField(default=False, verbose_name="Флаг приятной привычки")
    link_pleasant = models.ForeignKey("self", on_delete=models.SET_NULL, verbose_name='Связанная привычка', **NULLABLE)
    award = models.CharField(max_length=150, verbose_name="Вознаграждение за выполнение привычки", **NULLABLE)
    frequency = models.PositiveIntegerField(default=1, verbose_name='Периодичность привычки в днях')
    duration = models.PositiveIntegerField(default=120, verbose_name='Время на выполнения привычки')
    is_public = models.BooleanField(default=False, verbose_name='Флаг публикации')
    task = models.ForeignKey(PeriodicTask, on_delete=models.SET_NULL, verbose_name='Ссылка на периодическую задачу',
                             **NULLABLE)

    def __str__(self):
        loop_self = self
        message = f"я буду {self.action} в {self.time} в {self.place}\nВремя на выполнение: {self.duration}\n"
        while True:
            if loop_self.award:
                return message + f"Вознаграждение: {loop_self.award}"
            elif loop_self.link_pleasant is None:
                return message
            else:
                loop_self = loop_self.link_pleasant
                continue

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = 'Привычки'
