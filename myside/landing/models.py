from django.db import models


class Subscriber(models.Model):  # Создаем класс подпищиков
    # Создаем базу маил
    email = models.EmailField() #является ли значение действительным адресом электронной
    # Создаем базу имен с мах буквами 128
    name = models.CharField(max_length=128) #Строковое поле, для строк малого и большого размера.

    def __str__(self):  # Даная модель должна презинтовать запись
        # %S - подставление значения(типо .Format)
        return "Пользователь: %s, E-mail: %s" % (self.name, self.email)  # запись из этой модели возврощает ID

    # Меняет наименование из единственного во множественное (сами решаем как называть)
    class Meta:
        verbose_name = "MySubscriber"
        verbose_name_plural = "A lot of Subscribers"
