from django.urls import path, include
from . import views

app_name = 'categories'

urlpatterns = [
    path('', views.categories_list, name='categories_list'),
    path('<int:category_id>/', views.category_detail, name='category_detail'),
]