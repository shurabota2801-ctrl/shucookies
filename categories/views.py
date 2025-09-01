from django.shortcuts import get_object_or_404, render, redirect
from .models import Category
from recipes.models import Recipe
from django.contrib.auth.decorators import login_required

def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/categories_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    recipes = category.recipe_set.all()
    return render(request, 'categories/category_detail.html', {'category': category, 'recipes': recipes})

