from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    username = models.CharField(unique=True, max_length=20, verbose_name="Имя пользователя")
    email = models.EmailField(unique=True, max_length=50, verbose_name="Электронная почта")
    tg_chat_id = models.CharField(verbose_name="Телеграмм chat-id", unique=True, blank=True, null=True, max_length=100)
    phone_number = models.CharField(verbose_name="Номер телефона", blank=True, null=True, max_length=20)
    city = models.CharField(verbose_name="Город", blank=True, null=True, max_length=100)
    avatar = models.FileField(upload_to="avatars/", verbose_name="Ваша фотография", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        db_table = "users"

    def __str__(self):
        return f"{self.email}"
