from django.shortcuts import render
from recipes.models import Recipe

def search(request):
    query = request.GET.get('q')
    if query:
        recipes = Recipe.objects.filter(title__icontains=query)
    else:
        recipes = Recipe.objects.none()
    
    return render(request, 'recipes/search_results.html', {'recipes': recipes, 'query': query})
