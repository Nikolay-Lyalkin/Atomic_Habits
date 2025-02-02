from rest_framework.serializers import ModelSerializer

from habits.models import Habit, PleasantHabit
from habits.validators import CheckGoodHabit, CheckGoodHabitAndAward, CheckTimeOnComplete


class HabitSerializer(ModelSerializer):

    class Meta:
        model = Habit
        fields = "__all__"


class HabitCreateSerializer(ModelSerializer):

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            CheckGoodHabitAndAward(),
            CheckTimeOnComplete(),
        ]


class PleasantHabitSerializer(ModelSerializer):

    class Meta:
        model = PleasantHabit
        fields = "__all__"


class PleasantHabitCreateSerializer(ModelSerializer):

    class Meta:
        model = PleasantHabit
        fields = "__all__"
        validators = [CheckGoodHabit()]
