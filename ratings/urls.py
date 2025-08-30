from django.urls import path
from . import views

app_name = 'ratings'

urlpatterns = [
    path('recipe/<int:recipe_id>/add-rating/', views.add_rating, name='add_rating'),
]