from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitListView, HabitDetailView, HabitCreateView, HabitUpdateView, HabitDeleteView, \
    PublicHabitListView

app_name = HabitsConfig.name

urlpatterns = [
    path("create/", HabitCreateView.as_view(), name="habit_create"),
    path("public/", PublicHabitListView.as_view(), name="habits_public_list"),
    path("list/", HabitListView.as_view(), name="habits_list"),
    path("<int:pk>/", HabitDetailView.as_view(), name="habit_detail"),
    path("<int:pk>/update/", HabitUpdateView.as_view(), name="habit_update"),
    path("<int:pk>/delete/", HabitDeleteView.as_view(), name="habit_delete"),
]
