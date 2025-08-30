from django.shortcuts import render, get_object_or_404
from recipes.models import Recipe
from ratings.forms import RatingForm

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ratings = recipe.ratings.all().order_by('-created_at')[:5]
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

