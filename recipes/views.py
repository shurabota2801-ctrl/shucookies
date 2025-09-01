from django.shortcuts import render, get_object_or_404, redirect
from recipes.models import Recipe
from ratings.forms import RatingForm
from ratings.models import Rating
from django.contrib.auth.decorators import login_required

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ratings = recipe.ratings.all().order_by('-created_at')[:5]
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = RatingForm(request.POST)
        if form.is_valid():
            # Проверяем, не оставил ли пользователь уже отзыв
            if Rating.objects.filter(recipe=recipe, user=request.user).exists():
                return redirect('recipes:recipe_detail', recipe_id=recipe_id)
            
            # Сохраняем новый отзыв
            rating = form.save(commit=False)
            rating.recipe = recipe
            rating.user = request.user
            rating.save()
            return redirect('recipes:recipe_detail', recipe_id=recipe_id)
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

def search(request):
    query = request.GET.get('q')
    if query:
        recipes = Recipe.objects.filter(title__icontains=query)
    else:
        recipes = Recipe.objects.none()
    
    return render(request, 'recipes/search_results.html', {'recipes': recipes, 'query': query})


