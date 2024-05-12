from django.urls import path, include
from retailers.apps import RetailersConfig
from retailers.views import NetworkNodeCreateAPIView

app_name = RetailersConfig.name


urlpatterns = [
    path('create-retailer/', NetworkNodeCreateAPIView.as_view(), name='create-retailer'),
]
