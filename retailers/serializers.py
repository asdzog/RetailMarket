from rest_framework import serializers

from retailers.models import Contact, Product, NetworkNode


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class NetworkNodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'
