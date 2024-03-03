from django.shortcuts import render

from ledger.models import Recipe, RecipeIngredient


def recipes_list(request):
    recipe_list = {"recipe_list": Recipe.objects.all()}

    return render(request, 'recipes_list.html', recipe_list)


def recipe(request, pk):
    recipe_name = Recipe.objects.get(pk=pk)
    recipe_detail = { 'ingredients': RecipeIngredient.objects.filter(recipe__name=recipe_name)}

    return render(request, 'recipe.html', recipe_detail)

