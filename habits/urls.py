from django.urls import path

from . import views
from .apps import HabitsConfig

app_name = HabitsConfig.name

urlpatterns = [
    # habits
    path("publicity_habits/", views.PublicityHabitListAPIView.as_view(), name="publicity_habit_list"),
    path("habits/", views.HabitListAPIView.as_view(), name="habit_list"),
    path("habit/create/", views.HabitCreateAPIView.as_view(), name="habit_create"),
    path("habit/<int:pk>/update/", views.HabitUpdateAPIView.as_view(), name="habit_update"),
    path("habit/<int:pk>/delete/", views.HabitDeleteAPIView.as_view(), name="habit_delete"),
    path("habit/<int:pk>/", views.HabitRetrieveAPIView.as_view(), name="habit_retrieve"),
    # pleasant_habits
    path("pleasant_habits/", views.PleasantHabitListAPIView.as_view(), name="pleasant_habit_list"),
    path(
        "publicity_pleasant_habits/",
        views.PublicityPleasantHabitListAPIView.as_view(),
        name="publicity_pleasant_habit_list",
    ),
    path("pleasant_habit/create/", views.PleasantHabitCreateAPIView.as_view(), name="pleasant_habit_create"),
    path("pleasant_habit/<int:pk>/update/", views.PleasantHabitUpdateAPIView.as_view(), name="pleasant_habit_update"),
    path("pleasant_habit/<int:pk>/delete/", views.PleasantHabitDeleteAPIView.as_view(), name="pleasant_habit_delete"),
    path("pleasant_habit/<int:pk>/", views.PleasantHabitRetrieveAPIView.as_view(), name="pleasant_habit_retrieve"),
]
