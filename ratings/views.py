from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from recipes.models import Recipe
from .models import Rating
from .forms import RatingForm

@login_required
def add_rating(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            if Rating.objects.filter(recipe=recipe, user=request.user).exists():
                return redirect('categories:recipe_detail', recipe_id=recipe_id)
            
            # Сохраняем новый отзыв
            rating = form.save(commit=False)
            rating.recipe = recipe
            rating.user = request.user
            rating.save()
            return redirect('categories:recipe_detail', recipe_id=recipe_id)
    else:
        form = RatingForm()
    
    return render(request, 'recipes/recipe_detail.html', {
        'form': form,
        'recipe': recipe
    })