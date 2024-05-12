from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from retailers.serializers import ProductSerializer, ContactSerializer, NetworkNodeSerializer


# Create your views here.
class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ContactCreateAPIView(generics.CreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]


class NetworkNodeCreateAPIView(generics.CreateAPIView):
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsAuthenticated]
