from django.contrib import admin
from .models import Order, Status, PoductInOrder, PoductInBasket


class PoductInOrderInline(admin.TabularInline):
    model = PoductInOrder
    extra = 0


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]  # создание всех сталбцов имя и мэил и ip

    class Meta:
        model = Status #название


admin.site.register(Status, StatusAdmin)  # регистрируем статус и админов


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]  # создание всех сталбцов имя и мэил и ip
    inlines = [PoductInOrderInline]

    class Meta:
        model = Order #название


admin.site.register(Order, OrderAdmin)  # регистрируем заказы и админов


class PoductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PoductInOrder._meta.fields]  # создание всех сталбцов имя и мэил и ip

    class Meta:
        model = PoductInOrder #название


admin.site.register(PoductInOrder, PoductInOrderAdmin)  # регистрируем продукты в заказе и админов

class PoductInBasketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PoductInBasket._meta.fields]  # создание всех сталбцов имя и мэил и ip

    class Meta:
        model = PoductInBasket #название


admin.site.register(PoductInBasket, PoductInBasketAdmin)