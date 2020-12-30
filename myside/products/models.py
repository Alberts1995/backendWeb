from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)# поле можно оставить пустым,  хранить пустые значения как NULL в базе данных, вызываемое поле
    is_active = models.BooleanField(default=True)#вызываемое поле

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категория товаров'


class Product(models.Model):  # Создаем класс продукт
    # Создаем базу имен с мах буквами 64
    name = models.CharField(max_length=64, blank=True, null=True, default=None)# поле можно оставить пустым,  хранить пустые значения как NULL в базе данных, вызываемое поле
    # цена на товар
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)# макс цена, число после запятой
    # скидка
    discount = models.IntegerField(default=0)#вызываемое поле
    # категории
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)# отношение многие к одному поле можно оставить пустым,  хранить пустые значения как NULL в базе данных, вызываемое поле
    # Создание описания продукта
    description = models.TextField(blank=True, null=True, default=None)#поле можно оставить пустым,  хранить пустые значения как NULL в базе данных, вызываемое поле
    short_description = models.TextField(blank=True, null=True, default=None)#поле можно оставить пустым,  хранить пустые значения как NULL в базе данных, вызываемое поле
    # Создание заказа
    created = models.DateTimeField(auto_now_add=True, auto_now=False) #создания или обновления
    # Обновление заказа
    updated = models.DateTimeField(auto_now_add=False, auto_now=True) #создания или обновления
    is_active = models.BooleanField(default=True)

    def __str__(self):  # Даная модель должна презинтовать запись
        # %S - подставление значения(типо .Format)
        return "Продукт: %s" % self.name  # запись из этой модели возврощает ID

    # Меняет наименование из единственного во множественное (сами решаем как называть)
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class ProductImage(models.Model):  # Создаем класс картинки
    # Ссылка на продукт
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.DO_NOTHING) # отношение многие к одному поле можно оставить пустым,  хранить пустые значения как NULL в базе данных, вызываемое поле
    # Создание картинки
    image = models.ImageField(upload_to='product_img/') #загруженный объект является допустимым изображением.
    # Выбор отоброжать ли картинку
    is_active = models.BooleanField(default=True)#вызываемое поле
    is_main = models.BooleanField(default=False)#вызываемое поле
    # Создание заказа
    created = models.DateTimeField(auto_now_add=True, auto_now=False) #создания или обновления
    # Обновление заказа
    updated = models.DateTimeField(auto_now_add=False, auto_now=True) #создания или обновления

    def __str__(self):  # Даная модель должна презинтовать запись
        # %S - подставление значения(типо .Format)
        return "Фото: %s" % self.id  # запись из этой модели возврощает ID

    # Меняет наименование из единственного во множественное (сами решаем как называть)
    class Meta:
        verbose_name = "Фоторафия"
        verbose_name_plural = "Фотографии"
