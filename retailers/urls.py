from django.urls import path
from retailers.apps import RetailersConfig
from retailers.views import NetworkNodeCreateAPIView, ContactListAPIView, ProductListAPIView, NetworkNodeListAPIView, \
    NetworkNodeDeleteAPIView, NetworkNodeUpdateAPIView, NetworkNodeRetrieveAPIView

app_name = RetailersConfig.name


urlpatterns = [
    path('create/', NetworkNodeCreateAPIView.as_view(), name='create'),
    path('<int:pk>/details/', NetworkNodeRetrieveAPIView.as_view(), name='details'),
    path('<int:pk>/update/', NetworkNodeUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', NetworkNodeDeleteAPIView.as_view(), name='delete'),
    path('', NetworkNodeListAPIView.as_view(), name='list'),
    path('contacts/', ContactListAPIView.as_view(), name='contacts'),
    path('products/', ProductListAPIView.as_view(), name='products'),
]
