from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from categories.models import Category

class Recipe(models.Model):
   title = models.CharField(max_length=200, verbose_name='Название рецепта')
   author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
   category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория')
   description = models.TextField(verbose_name='Описание')
   cooking_time = models.PositiveIntegerField(verbose_name='Время приготовления (мин)')
   servings = models.PositiveIntegerField(verbose_name='Количество порций')
   image = models.ImageField(upload_to='recipes/', blank=True, null=True, verbose_name='Изображение')
   created_at = models.DateTimeField(auto_now_add=True)
   updated_to = models.DateTimeField(auto_now=True)

   class Meta:
       verbose_name = 'Рецепт'
       verbose_name_plural = 'Рецепты'
  
   def __str__(self):
       return self.title
  
class Ingredient(models.Model):
   recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
   name = models.CharField(max_length=100, verbose_name='Название ингредиента')
   quantity = models.CharField(max_length=50, verbose_name='Количество')
   unit = models.CharField(max_length=20, blank=True, verbose_name='Единица измерения')

   class Meta:
       verbose_name = 'Ингредиент'
       verbose_name_plural = 'Ингредиенты'

   def __str__(self):
       return f"{self.name} - {self.quantity} {self.unit}"
  
class CookingStep(models.Model):
   recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='steps')
   step_number = models.PositiveIntegerField(verbose_name='Номер шага')
   description = models.TextField(verbose_name='Описание шага')
   image = models.ImageField(upload_to='steps/', blank=True, null=True, verbose_name='Изображение шага')

   class Meta:
       verbose_name = 'Шаг приготовления'
       verbose_name_plural = 'Шаги приготовления'
       ordering = ['step_number']

   def __str__(self):
       return f"Шаг {self.step_number} - {self.recipe.title}"