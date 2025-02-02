from rest_framework.test import APITestCase
from rest_framework import status

from habits.models import Habit, PleasantHabit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test", email="test@yandex.ru", password="testpass")
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
                                          user=self.user,
                                          action="Вечерняя прогулка",
                                          time="20:00:00",
                                          award="Фруктовая тарелка"
        )

    def test_habit_create(self):
        data = {
                "action": "Утренняя растяжка",
                "time": "08:00:00",
                "award": "Пирожное Rex"
                }

        response = self.client.post("/habit/create/", data=data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.json(), {'id': 3, 'place': None, 'time': '08:00:00', 'action': 'Утренняя растяжка', 'periodicity': 1, 'award': 'Пирожное Rex', 'time_to_complete': None, 'sign_publicity': None, 'user': 2, 'good_habit': None})
        self.assertTrue(Habit.objects.all().exists())

    def test_list_habit(self):


        response = self.client.get("/habits/")

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json(), {'count': 1, 'next': None, 'previous': None, 'results': [{'id': 4, 'place': None, 'time': '20:00:00', 'action': 'Вечерняя прогулка', 'periodicity': 1, 'award': 'Фруктовая тарелка', 'time_to_complete': None, 'sign_publicity': False, 'user': 3, 'good_habit': None}]})

    def test_delete_habit(self):

        response = self.client.delete("/habit/1/delete/")

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put_habit(self):

        data = {
            "action": "Вечерняя пробежка"
        }

        response = self.client.put("/habit/5/update/", data=data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json(), {'id': 5, 'place': None, 'time': '20:00:00', 'action': 'Вечерняя пробежка', 'periodicity': 1, 'award': 'Фруктовая тарелка', 'time_to_complete': None, 'sign_publicity': None, 'user': 4, 'good_habit': None})


class PleasantHabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", email="test@yandex.ru", password="testpass")
        self.client.force_authenticate(user=self.user)
        self.pleasant_habit = PleasantHabit.objects.create(user=self.user,
                                            action="Поход в Grammy",
                                            place="Grammy",
                                            sign_pleasant_habit="True"
                                            )

    def test_validator_pleasant_habit_create(self):
        data = {
                "action": "Утренний кофе",
                "place": "Шоколадница",
                }

        response = self.client.post("/pleasant_habit/create/", data=data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response.json(), {'non_field_errors': ['Могут быть добавлены привычки только с признаком приятной привычки']})

    def test_pleasant_habit_create(self):
        data = {
                "action": "Утренний кофе",
                "place": "Шоколадница",
                "sign_pleasant_habit": "True"
                }

        response = self.client.post("/pleasant_habit/create/", data=data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.json(), {'id': 3, 'place': 'Шоколадница', 'time': None, 'action': 'Утренний кофе', 'sign_pleasant_habit': True, 'sign_publicity': False, 'user': 6})
        self.assertTrue(PleasantHabit.objects.all().exists())

    def test_list_pleasant_habit(self):

        response = self.client.get("/pleasant_habits/")

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json(), {'count': 1, 'next': None, 'previous': None, 'results': [
            {'id': 1, 'place': 'Grammy', 'time': None, 'action': 'Поход в Grammy', 'sign_pleasant_habit': True,
             'sign_publicity': False, 'user': 5}]})
