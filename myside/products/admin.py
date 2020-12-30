from django.contrib import admin
from .models import Product, ProductImage, ProductCategory


class ProductImageInline(admin.TabularInline):
    model = ProductImage #название
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]  # создание всех сталбцов имя и мэил и ip
    inlines = [ProductImageInline]

    class Meta:
        model = Product #название


admin.site.register(Product, ProductAdmin)  # регистрируем подпищиков и


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]# создание всех сталбцов имя и мэил и ip

    class Meta:
        model = ProductCategory #название


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]  # создание всех сталбцов имя и мэил и ip

    class Meta:
        model = ProductImage #название


admin.site.register(ProductImage, ProductImageAdmin)  # регистрируем подпищиков и админов
