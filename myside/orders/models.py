from django.db import models
from products.models import Product
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Status(models.Model):  # Создаем класс cтатус
    # создание столбца имени
    name = models.CharField(max_length=24, blank=True, null=True, default=None) # поле можно оставить пустым,  хранить пустые значения как NULL в базе данных, вызываемое поле
    # Создание заказа
    created = models.DateTimeField(auto_now_add=True, auto_now=False)  #создания или обновления
    # Обновление заказа
    updated = models.DateTimeField(auto_now_add=False, auto_now=True) #создания или обновления

    is_active = models.BooleanField(default=True) #вызываемое поле

    def __str__(self):  # Даная модель должна презинтовать запись
        # %S - подставление значения(типо .Format)
        return "Статус: %s" % self.name  # запись из этой модели возврощает ID

    # Меняет наименование из единственного во множественное (сами решаем как называть)
    class Meta:
        verbose_name = "Статус заказа"
        verbose_name_plural = "Статусы заказа"


class Order(models.Model):  # Создаем класс заказ
    user = models.ForeignKey(User, blank=True, default=None, null=True, on_delete=models.DO_NOTHING)
    # Общая цена
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) # макс цена, число после запятой
    # Создаем базу имен с мах буквами 128 можно оставить пустое
    custemer_name = models.CharField(max_length=64, blank=True, null=True, default=None) # поле можно оставить пустым,  хранить пустые значения как NULL в базе данных, вызываемое поле
    # Создаем базу маил
    custemer_email = models.EmailField(blank=True, null=True, default=None) # поле можно оставить пустым,  хранить пустые значения как NULL в базе данных, вызываемое поле
    # Создание телефона, можно оставить пустое
    custemer_phone = models.CharField(max_length=48, blank=True, null=True, default=None) # поле можно оставить пустым,  хранить пустые значения как NULL в базе данных, вызываемое поле
    custemer_adress = models.CharField(max_length=128, blank=True, null=True, default=None) # поле можно оставить пустым,  хранить пустые значения как NULL в базе данных, вызываемое поле
    # Создание коментарий
    comments = models.TextField(blank=True, null=True, default=None) # поле можно оставить пустым,  хранить пустые значения как NULL в базе данных, вызываемое поле
    # Создание заказа
    created = models.DateTimeField(auto_now_add=True, auto_now=False) # поле можно оставить пустым,  хранить пустые значения как NULL в базе данных, вызываемое поле
    # Обновление заказа
    updated = models.DateTimeField(auto_now_add=True, auto_now=False) #создания или обновления
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING) # отношение многие к одному

    def __str__(self):  # Даная модель должна презинтовать запись
        # %S - подставление значения(типо .Format)
        return "Заказ: %s, %s" % (self.id, self.status.name)  # запись из этой модели возврощает ID

    # Меняет наименование из единственного во множественное (сами решаем как называть)
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class PoductInOrder(models.Model):  # Ссылка на товар
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)# отношение многие к одному поле можно оставить пустым,  хранить пустые значения как NULL в базе данных, вызываемое поле
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)# отношение многие к одному поле можно оставить пустым,  хранить пустые значения как NULL в базе данных, вызываемое поле
    # цена на товар Целое число
    nmb = models.IntegerField(default=1) #вызываемое поле
    # цена тогда и сейчас
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)#макс цена, число после запятой
    # цена всех товаров
    total_pice = models.DecimalField(max_digits=10, decimal_places=2, default=0)#макс цена, число после запятой
    is_active = models.BooleanField(default=True)#вызываемое поле
    created = models.DateTimeField(auto_now_add=True, auto_now=False)  # Создание заказа
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)  # Обновление заказа

    def __str__(self):  # Даная модель должна презинтовать запись
        # %S - подставление значения(типо .Format)
        return "Продукт: %s" % self.product.name  # запись из этой модели возврощает ID

    # Меняет наименование из единственного во множественное (сами решаем как называть)
    class Meta:
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказе"

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_pice = int(self.nmb) * self.price_per_item

        super(PoductInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = PoductInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_pice

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=PoductInOrder)


class PoductInBasket(models.Model):  # Ссылка на товар
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)# отношение многие к одному поле можно оставить пустым,  хранить пустые значения как NULL в базе данных, вызываемое поле
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)# отношение многие к одному поле можно оставить пустым,  хранить пустые значения как NULL в базе данных, вызываемое поле
    # цена на товар Целое число
    nmb = models.IntegerField(default=1) #вызываемое поле
    # цена тогда и сейчас
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)#макс цена, число после запятой
    # цена всех товаров
    total_pice = models.DecimalField(max_digits=10, decimal_places=2, default=0)#макс цена, число после запятой
    is_active = models.BooleanField(default=True)#вызываемое поле
    created = models.DateTimeField(auto_now_add=True, auto_now=False)  # Создание заказа
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)  # Обновление заказа

    def __str__(self):  # Даная модель должна презинтовать запись
        # %S - подставление значения(типо .Format)
        return "Продукт: %s" % self.product.name  # запись из этой модели возврощает ID

    # Меняет наименование из единственного во множественное (сами решаем как называть)
    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_pice = int(self.nmb) * self.price_per_item

        super(PoductInBasket, self).save(*args, **kwargs)
