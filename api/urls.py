from django.urls import path, include

from api.apps import ApiConfig
from users.views import UserCreateAPIView, UserProfileView

app_name = ApiConfig.name


urlpatterns = [
    path('users/', include('users.urls', namespace='users')),
    path('retailers/', include('retailers.urls', namespace='retailers')),
    # path('send-code/', AuthAPIView.as_view(), name='send_code'),
    # path('verify-phone/', VerifyPhoneAPIView.as_view(), name='verify_phone'),
]
