from django.db import models
from config import settings

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='название курса')
    text = models.TextField(verbose_name='описание')
    price = models.IntegerField(verbose_name='цена', default=10000)
    payment_url = models.TextField(verbose_name='ссылка для оплаты', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
