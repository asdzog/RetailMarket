from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import NetworkNode


class SupplierLevelValidator:

    def __init__(self, field_level='level', field_supplier='supplier'):
        self.field_level = field_level
        self.field_supplier = field_supplier

    def __call__(self, attrs):
        level = attrs.get(self.field_level, 0)
        supplier_id = attrs.get(self.field_supplier)

        if supplier_id:
            supplier = NetworkNode.objects.get(id=supplier_id)
            expected_level = supplier.level + 1
            if level != expected_level:
                raise serializers.ValidationError({self.field_level: f"Уровень должен быть {expected_level}."})
        elif level != 0:
            raise serializers.ValidationError(
                {self.field_level: "Уровень должен быть 0 для узлов сети без поставщика."})
