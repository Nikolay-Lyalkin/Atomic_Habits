from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "tg_chat_id", "phone_number"]


class UserCreateSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "email", "tg_chat_id", "phone_number", "is_superuser"]
