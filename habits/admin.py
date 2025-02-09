from django.contrib import admin

from habits.models import Habit, PleasantHabit


@admin.register(Habit)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user", "action", "good_habit", "award", "time_to_complete")


@admin.register(PleasantHabit)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user", "action")
