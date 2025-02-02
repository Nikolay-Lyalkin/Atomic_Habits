from rest_framework.test import APITestCase
from rest_framework import status

from habits.models import Habit
from users.models import User


class HabitsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test", email="test@yandex.ru", password="testpass")
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
                                          action="Вечерняя прогулка",
                                          time="20:00:00",
                                          award="Фруктовая тарелка")

    def test_habit_create(self):
        data = {
                "action": "Утренняя растяжка",
                "time": "08:00:00",
                "award": "Пирожное Rex"
                }

        response = self.client.post("/habit/create/", data=data)
        print(response.json())

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        self.assertEquals(response.json(), {'id': 2, 'place': None, 'time': '08:00:00', 'action': 'Утренняя растяжка', 'periodicity': 1, 'award': 'Пирожное Rex', 'time_to_complete': None, 'sign_publicity': None, 'user': 1, 'good_habit': None})

        self.assertTrue(Habit.objects.all().exists())
