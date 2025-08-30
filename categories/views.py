from django.shortcuts import get_object_or_404, render, redirect
from .models import Category
from recipes.models import Recipe
from ratings.models import Rating
from ratings.forms import RatingForm
from django.contrib.auth.decorators import login_required

def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/categories_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    recipes = category.recipe_set.all()
    return render(request, 'categories/category_detail.html', {'category': category, 'recipes': recipes})

def category_this_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ratings = recipe.ratings.all().order_by('-created_at')
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = RatingForm(request.POST)
        if form.is_valid():
            if Rating.objects.filter(recipe=recipe, user=request.user).exists():
                return redirect('categories:recipe_detail', recipe_id=recipe_id)
            
            rating = form.save(commit=False)
            rating.recipe = recipe
            rating.user = request.user
            rating.save()
            return redirect('categories:recipe_detail', recipe_id=recipe_id)
    else:
        form = RatingForm()
    
    return render(
        request, 
        'recipes/recipe_detail.html', 
        {
            'recipe': recipe,
            'ratings': ratings,
            'form': form
        }
    )
