from django.urls import path, include

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserProfileView

app_name = UsersConfig.name


urlpatterns = [
    path('create-user/', UserCreateAPIView.as_view(), name='create-user'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
]
