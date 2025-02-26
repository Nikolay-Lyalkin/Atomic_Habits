from django.db import models

from users.models import User


class PleasantHabit(models.Model):
    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="user_pleasant_habit",
        verbose_name="пользователь",
    )
    place = models.CharField(verbose_name="Место", blank=True, null=True, max_length=250)
    time = models.CharField(verbose_name="Время", blank=True, null=True, max_length=1000)
    action = models.CharField(verbose_name="Действие", max_length=1000)
    sign_pleasant_habit = models.BooleanField(verbose_name="Признак приятной привычки", default=True)
    sign_publicity = models.BooleanField(verbose_name="Публикация в общий доступ", default=False)

    def __str__(self):
        return f"{self.action}"

    class Meta:
        verbose_name = "Приятная привычка"
        verbose_name_plural = "Приятные привычки"
        db_table = "pleasant_habits"


class Habit(models.Model):
    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="user_habit",
        verbose_name="пользователь",
    )
    place = models.CharField(verbose_name="Место", blank=True, null=True, max_length=250)
    time = models.TimeField(verbose_name="Время", default="12:00", blank=True, null=True, max_length=1000)
    action = models.CharField(verbose_name="Действие", max_length=1000)
    good_habit = models.ForeignKey(
        PleasantHabit,
        verbose_name="Приятная привычка",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="pleasant_habit",
    )
    periodicity = models.PositiveIntegerField(verbose_name="Периодичность в неделю", default=1, blank=True, null=True)
    award = models.CharField(verbose_name="Вознаграждение", blank=True, null=True, max_length=1000)
    time_to_complete = models.PositiveIntegerField(
        verbose_name="Время на выполнение в секундах", blank=True, null=True
    )
    sign_publicity = models.BooleanField(
        verbose_name="Признак публичной привычки", default=False, blank=True, null=True
    )

    def __str__(self):
        return f"{self.action}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        db_table = "habits"
