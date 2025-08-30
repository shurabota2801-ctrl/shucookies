from django.urls import path, include
from . import views

app_name = 'recipes'

urlpatterns = [
        path('search/', views.search, name='search'),
        path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
]