from django.db import models
from config import settings
from materials.models import Materials

NULLABLE = {'blank': True, 'null': True}


class Testing_info(models.Model):
    question = models.CharField(max_length=100, verbose_name='вопрос для теста')
    materials = models.ForeignKey(Materials, on_delete=models.CASCADE, verbose_name='материал')
    answer = models.CharField(max_length=100, verbose_name='ответ для теста', **NULLABLE)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'


class Answer_user(models.Model):
    answer = models.CharField(max_length=100, verbose_name='ответ пользователя', **NULLABLE)
    test = models.ForeignKey(Testing_info, on_delete=models.CASCADE, verbose_name='ответ пользователя')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             verbose_name='пользователь', related_name='user', **NULLABLE)
