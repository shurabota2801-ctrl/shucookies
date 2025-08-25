from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(
        blank=True, 
        verbose_name='Биография'
    )
    avatar = models.ImageField(
        blank=True, 
        null=True,
        upload_to='users/avatars/%Y/%m/%d/',
        verbose_name='Аватар'
    )
    experience = models.PositiveIntegerField(
        default=0,
        verbose_name='Опыт (лет)'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
    def __str__(self):
        return self.username