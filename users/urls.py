from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserProfileView

app_name = UsersConfig.name


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('create-user/', UserCreateAPIView.as_view(), name='create-user'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
]
