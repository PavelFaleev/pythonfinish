from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecipeForm
from .models import Recipe
from django.shortcuts import render

# Главная страница, список рецептов
def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/home.html', {'recipes': recipes})

# Страница добавления нового рецепта
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipes_list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})

# Страница списка рецептов
def recipes_list(request):
    recipes = Recipe.objects.all()  # Получаем все рецепты из базы данных
    return render(request, 'recipes/recipes_list.html', {'recipes': recipes})

# Страница с подробной информацией о рецепте
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
