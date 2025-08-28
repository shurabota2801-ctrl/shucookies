from django.shortcuts import render, get_object_or_404
from .models import Category
from recipes.models import Recipe

def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/categories_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    recipes = category.recipe_set.all()
    return render(request, 'categories/category_detail.html', {'category': category, 'recipes': recipes})

def category_this_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
