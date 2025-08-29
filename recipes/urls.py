from django.urls import path, include
from . import views

app_name = 'recipes'

urlpatterns = [
        path('search/', views.search, name='search'),
]