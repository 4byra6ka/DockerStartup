from rest_framework.serializers import ValidationError

from habits.models import Habit


class DurationValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        field_value = dict(value).get(self.field)
        if field_value is not None:
            if field_value > 120:
                raise ValidationError('Время выполнения должно быть не больше 120 секунд.')


class FrequencyValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        field_value = dict(value).get(self.field)
        if field_value is not None:
            if field_value > 7:
                raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')


class IsPleasantValidator:

    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, value):
        is_pleasant = dict(value).get(self.field1)
        link_pleasant = dict(value).get(self.field2)
        award = dict(value).get(self.field3)
        if link_pleasant is not None and award is not None:
            raise ValidationError('Невозможен одновременный выбор связанной привычки и указания вознаграждения.')
        if link_pleasant is not None:
            link_pleasant_obj = Habit.objects.filter(pk=link_pleasant.pk, is_pleasant=True)
            if len(link_pleasant_obj) == 0:
                raise ValidationError(
                    'В связанные привычки могут попадать только привычки с признаком приятной привычки.')
        if is_pleasant and link_pleasant is not None and award is not None:
            raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')
