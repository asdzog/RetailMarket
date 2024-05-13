import logging
from rest_framework import serializers
from retailers.models import Contact, Product, NetworkNode
from retailers.validators import SupplierLevelValidator


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'model', 'release_date']

    def validate(self, data):
        # Проверяем, существует ли продукт с таким ID
        if 'id' in data:
            if not Product.objects.filter(id=data['id']).exists():
                raise serializers.ValidationError({"id": "Product with this ID does not exist."})
            if len(data) == 1:
                # Если передан только ID, возвращаем данные без изменений
                return data
        # Проверка для создания нового продукта
        if not all(key in data for key in ['name', 'model', 'release_date']):
            raise serializers.ValidationError("All fields 'name', 'model', and 'release_date' must be included for new products.")
        return data

    def create(self, validated_data):
        # Создание нового продукта, если не предоставлен ID
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Обновление существующего продукта, изменение только переданных полей
        instance.name = validated_data.get('name', instance.name)
        instance.model = validated_data.get('model', instance.model)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.save()
        return instance


class NetworkNodeSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = NetworkNode
        fields = ['name', 'contact', 'products']
        validators = [SupplierLevelValidator('level', 'supplier')]

    def validate_debt(self, value):
        if self.instance and self.instance.debt != value:
            raise serializers.ValidationError("Обновление поля задолженности запрещено.")
        return value

    def create(self, validated_data):
        contact_data = validated_data.pop('contact', None)
        products_data = validated_data.pop('products', [])

        contact = Contact.objects.create(**contact_data) if contact_data else None
        network_node = NetworkNode.objects.create(contact=contact, **validated_data)

        for product_data in products_data:
            product, _ = Product.objects.get_or_create(**product_data)
            network_node.products.add(product)

        return network_node

    def update(self, instance, validated_data):
        # Аналогичная логика для обновления узла, если требуется
        return super().update(instance, validated_data)