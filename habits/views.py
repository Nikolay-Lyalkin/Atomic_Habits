from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit, PleasantHabit
from habits.paginators import PaginationHabits
from habits.permissions import IsOwner
from habits.serializers import (
    HabitCreateSerializer,
    HabitSerializer,
    PleasantHabitCreateSerializer,
    PleasantHabitSerializer,
)


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = PaginationHabits
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user)


class PublicityHabitListAPIView(generics.ListAPIView):
    queryset = Habit.objects.filter(sign_publicity=True)
    serializer_class = HabitSerializer
    pagination_class = PaginationHabits
    permission_classes = [IsAuthenticated]


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitUpdateAPIView(generics.UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitCreateSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDeleteAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        publicity = self.get_object().sign_publicity
        user = request.user
        if publicity or self.get_object().user == user:
            return self.retrieve(request, *args, **kwargs)


class PleasantHabitListAPIView(generics.ListAPIView):
    queryset = PleasantHabit.objects.all()
    serializer_class = PleasantHabitSerializer
    pagination_class = PaginationHabits
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return PleasantHabit.objects.filter(user=user)


class PublicityPleasantHabitListAPIView(generics.ListAPIView):
    queryset = PleasantHabit.objects.filter(sign_publicity=True)
    serializer_class = PleasantHabitSerializer
    pagination_class = PaginationHabits
    permission_classes = [IsAuthenticated]


class PleasantHabitCreateAPIView(generics.CreateAPIView):
    serializer_class = PleasantHabitCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PleasantHabitUpdateAPIView(generics.UpdateAPIView):
    queryset = PleasantHabit.objects.all()
    serializer_class = PleasantHabitCreateSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class PleasantHabitDeleteAPIView(generics.DestroyAPIView):
    queryset = PleasantHabit.objects.all()
    serializer_class = PleasantHabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class PleasantHabitRetrieveAPIView(generics.RetrieveAPIView):
    queryset = PleasantHabit.objects.all()
    serializer_class = PleasantHabitSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        publicity = self.get_object().sign_publicity
        user = request.user
        if publicity or self.get_object().user == user:
            return self.retrieve(request, *args, **kwargs)
