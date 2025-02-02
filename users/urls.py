from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views
from .apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    # User
    path("users/", views.UserListAPIView.as_view(), name="user_list"),
    path("user/create/", views.UserCreateAPIView.as_view(), name="user_create"),
    path("user/<int:pk>/update/", views.UserUpdateAPIView.as_view(), name="user_update"),
    path("user/<int:pk>/delete/", views.UserDeleteAPIView.as_view(), name="user_delete"),
    path("user/<int:pk>/", views.UserRetrieveAPIView.as_view(), name="user_retrieve"),
    path("user/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("user/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
