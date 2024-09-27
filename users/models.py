from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

NULLABLE = {'blank': True, 'null': True}



class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=True)
    phone = PhoneNumberField(verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    country = models.CharField(max_length=20, verbose_name='Страна', **NULLABLE)
    token = models.CharField(max_length=100, verbose_name='токен', **NULLABLE )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email