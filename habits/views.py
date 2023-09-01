from rest_framework import status
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.serializers import HabitSerializer
from habits.services import create_periodic_task
from habits.permissions import IsOwner


class HabitCreateView(CreateAPIView):
    """Контроллер создания привычки"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.task = create_periodic_task(new_habit.frequency, new_habit.pk, new_habit.time)
        new_habit.save()


class HabitListView(ListAPIView):
    """Контроллер списка привычек"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated & IsOwner]
    pagination_class = HabitPaginator

    def get_queryset(self):
        if self.request.user.is_staff:
            return Habit.objects.all().order_by("pk")
        else:
            return Habit.objects.filter(owner=self.request.user).order_by("pk")


class HabitDetailView(RetrieveAPIView):
    """Контроллер описания привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated & IsOwner]


class HabitUpdateView(UpdateAPIView):
    """Контроллер обновления привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated & IsOwner]

    def perform_update(self, serializer):
        update_habit = serializer.save()
        update_habit.task.delete()
        update_habit.task = create_periodic_task(update_habit.frequency, update_habit.pk, update_habit.time)
        update_habit.save()


class HabitDeleteView(DestroyAPIView):
    """Контроллер удаления привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated & IsOwner]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if len(Habit.objects.filter(link_pleasant=instance)) > 0:
            return Response({'error_message': 'Это связанная привычка не могу удалить'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.task.delete()
        instance.delete()


class PublicHabitListView(ListAPIView):
    """Контроллер списка публичных привычек"""
    queryset = Habit.objects.filter(is_public=True).order_by('pk')
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
