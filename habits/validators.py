from rest_framework import serializers


class CheckGoodHabitAndAward:
    """Проверка, что не может быть одновременно вознаграждение и приятная привычка"""

    def __call__(self, value):
        good_habit = dict(value).get("good_habit")
        award = dict(value).get("award")
        if good_habit and award:
            raise serializers.ValidationError(
                "Не может быть одновременно добавлена 'приятная привычка' и 'вознаграждение'"
            )


class CheckTimeOnComplete:
    """Проверка, что время на выполнение привычки не может превышать 120 секунд"""

    def __call__(self, value):
        time_to_complete = dict(value).get("time_to_complete")
        if time_to_complete:
            if int(time_to_complete) > 120:
                raise serializers.ValidationError("Время на выполнение не должно превышать 120 секунд")


class CheckGoodHabit:
    """Проверка, что в приятные привычки могут быть добавлены только те, что имеют признак приятной привычки"""

    def __call__(self, value):
        sign_pleasant_habit = dict(value).get("sign_pleasant_habit")

        if not sign_pleasant_habit:
            raise serializers.ValidationError("Могут быть добавлены привычки только с признаком приятной привычки")


class CheckPeriodicity:
    """Проверка, чтто периодичность привычки не может быть меньше одного раза в неделю"""

    def __call__(self, value):
        periodicity = dict(value).get("periodicity")
        if periodicity == 0:
            raise serializers.ValidationError("Периодичность не может быть меньше одного раза в неделю")
