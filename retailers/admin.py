from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import NetworkNode, Contact, Product


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'supplier_link', 'get_city', 'debt')
    list_filter = ('contact__city',)  # Фильтрация по городу контакта
    search_fields = ('name', 'contact__city')  # Поиск по имени и городу
    actions = ['clear_debts']

    def supplier_link(self, obj):
        if obj.supplier:
            link = reverse("admin:retailers_networknode_change", args=[obj.supplier.pk])
            return format_html('<a href="{}">{}</a>', link, obj.supplier.name)
        return '-'

    supplier_link.short_description = 'Поставщик'

    def get_city(self, obj):
        return obj.contact.city if obj.contact else '-'
    get_city.short_description = 'City'

    def clear_debts(self, request, queryset):
        queryset.update(debt=0)

    clear_debts.short_description = "Очистка долга перед поставщиком выбранных участников торговой сети"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house_number')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')
    search_fields = ('name', 'model')
