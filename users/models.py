from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from course.models import Course


NULLABLE = {'blank': True, 'null': True}


class UserRole(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    DoesNotExist = None
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    FIO = models.CharField(max_length=300, verbose_name='ФИО', **NULLABLE)
    role = models.CharField(max_length=50, choices=UserRole.choices, default=UserRole.MEMBER)
    is_active = models.BooleanField(default=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
