from django.contrib import admin
from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    # list_display = ["name", "email"] # создание 2 сталбцов имя и мэил
    list_display = [field.name for field in Subscriber._meta.fields]  # создание 3 сталбцов имя и мэил и ip
    list_filter = ("name",)  # Создание колонки с боку с именами (если есть одинаковые он засунит в один)
    # exclude = ["email"] # удаление в записи эмэил
    #fields = ["email"]  # показывать только эмэил
    # inlines = [FielMappingInline]
    search_fields = ["email"]  # Создание колонки поиска по мэилу

    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)  # регистрируем подпищиков и админов
