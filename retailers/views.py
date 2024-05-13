from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from retailers.models import Product, Contact, NetworkNode
from retailers.serializers import ProductSerializer, ContactSerializer, NetworkNodeSerializer
from users.permissions import IsActiveModer


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActiveModer]


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActiveModer]


class ContactCreateAPIView(generics.CreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated, IsActiveModer]


class ContactListAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated, IsActiveModer]


class NetworkNodeCreateAPIView(generics.CreateAPIView):
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsAuthenticated, IsActiveModer]


class NetworkNodeRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = NetworkNodeSerializer
    queryset = NetworkNode.objects.all()
    permission_classes = [IsAuthenticated, IsActiveModer]


class NetworkNodeUpdateAPIView(generics.UpdateAPIView):
    serializer_class = NetworkNodeSerializer
    queryset = NetworkNode.objects.all()
    permission_classes = [IsAuthenticated, IsActiveModer]


class NetworkNodeDeleteAPIView(generics.DestroyAPIView):
    queryset = NetworkNode.objects.all()
    permission_classes = [IsAuthenticated, IsActiveModer]


class NetworkNodeListAPIView(generics.ListAPIView):
    serializer_class = NetworkNodeSerializer
    queryset = NetworkNode.objects.all()
    permission_classes = [IsAuthenticated, IsActiveModer]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['contact__country']
