from django.db import models
from course.models import Course

NULLABLE = {'blank': True, 'null': True}


class Materials(models.Model):
    name = models.CharField(max_length=100, verbose_name='название урока')
    text = models.TextField(verbose_name='описание')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE,
                               related_name='materials')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
