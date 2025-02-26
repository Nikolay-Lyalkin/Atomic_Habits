from django.contrib import admin

from habits.models import Habit, PleasantHabit


@admin.register(Habit)
class UserAdminHabit(admin.ModelAdmin):
    list_display = ("user", "action", "good_habit", "award", "time_to_complete")


@admin.register(PleasantHabit)
class UserAdminPleasantHabit(admin.ModelAdmin):
    list_display = ("user", "action")
