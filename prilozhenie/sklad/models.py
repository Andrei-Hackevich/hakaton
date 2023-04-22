from django.db import models


class Tovar(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    description = models.TextField(verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    amount = models.IntegerField(verbose_name='Количество')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Поступило')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ('-published',)


class Client(models.Model):
    title = models.CharField(max_length=150, verbose_name='Клиент')
    adress = models.TextField(verbose_name='Адрес клиента')
    description = models.TextField(null=True, blank=True, verbose_name='Особенности клиента')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    order_1 = models.ManyToManyField(Tovar, through='Order')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'
        ordering = ('title',)

class Order(models.Model):
    tovar = models.ForeignKey(Tovar, on_delete=models.PROTECT, verbose_name='Товар')
    client = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name='Клиент')
    amount = models.IntegerField(default=0, verbose_name='Количество')
    status = models.BooleanField(default=False, verbose_name='Статус')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата заказа')

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'
        ordering = ('-published',)