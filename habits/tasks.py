from datetime import datetime

from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def remind_of_habit_with_time():
    """Напоминание о привычке с указанным врменем"""
    habits = Habit.objects.filter(time__isnull=False)
    time_now = datetime.now().hour
    for habit in habits:
        if habit.user.tg_chat_id:
            time_difference = habit.time.hour - time_now
            if time_difference == 1:
                message = f"До вашей полезной привычки '{habit.action}' осталось совсем немного времени, начало \
                 в {habit.time}. Вам необходимо сделать это не меньше {habit.periodicity} раз в неделю."
                send_telegram_message(habit.user.tg_chat_id, message)


@shared_task
def remind_of_habit_without_time():
    habits = Habit.objects.filter(time__isnull=True)

    for habit in habits:
        if habit.user.tg_chat_id:
            message = f"Если Вы выполнили привычку -'{habit.action}' меньше {habit.periodicity} раз(раза) в неделю, \
             сделай это сегодня!"
            send_telegram_message(habit.user.tg_chat_id, message)
