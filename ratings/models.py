from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe
from django.conf import settings

class Rating(models.Model):
    STAR_1 = 1
    STAR_2 = 2
    STAR_3 = 3
    STAR_4 = 4
    STAR_5 = 5
    
    RATING_CHOICES = [
        (STAR_1, '1 звезда'),
        (STAR_2, '2 звезды'),
        (STAR_3, '3 звезды'),
        (STAR_4, '4 звезды'),
        (STAR_5, '5 звезд')
    ]
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, verbose_name="Оценка")
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
        unique_together = ['recipe', 'user']

    def __str__(self):
        return f"{self.rating} звезд - {self.recipe.title}"