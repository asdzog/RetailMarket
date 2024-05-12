from django.core.exceptions import ValidationError
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название продукта")
    model = models.CharField(max_length=200, verbose_name="Модель продукта")
    release_date = models.DateField(verbose_name="Дата релиза")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Contact(models.Model):
    """Модель для хранения контактных данных"""
    email = models.EmailField(verbose_name="Email для контактов")
    phone = PhoneNumberField(unique=True, blank=True, verbose_name="Телефон")
    country = models.CharField(max_length=50, verbose_name="Страна")
    city = models.CharField(max_length=50, verbose_name="Город")
    street = models.CharField(verbose_name="Улица")
    house_number = models.CharField(verbose_name="Номер дома")

    def __str__(self):
        return f"{self.email} - {self.country}, {self.city}"

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class NetworkNode(models.Model):
    """ МОдель узла сети продаж """

    name = models.CharField(max_length=250, verbose_name="Название")
    description = models.TextField(max_length=250, **NULLABLE, verbose_name="Описание")
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, verbose_name="Контакты")
    products = models.ManyToManyField(to=Product, verbose_name="Продукты ритейлера")
    supplier = models.ForeignKey("self", on_delete=models.SET_NULL, **NULLABLE, verbose_name="Поставщик")
    debt = models.DecimalField(max_digits=10, decimal_places=2, **NULLABLE, verbose_name="Долг перед поставщиком")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата/время занесения в базу")
    level = models.IntegerField(default=0, verbose_name="Уровень иерархии сети")

    def clean(self):
        if self.supplier and self.level != self.supplier.level + 1:
            raise ValidationError(
                f"Уровень должен быть {self.supplier.level + 1}, т.к. поставщик имеет уровень {self.supplier.level}.")
        if not self.supplier and self.level != 0:
            raise ValidationError("Уровень должен быть 0 для узлов сети без поставщика.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Ритейлер'
        verbose_name_plural = 'Ритейлеры'

