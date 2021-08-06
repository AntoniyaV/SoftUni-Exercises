from django.shortcuts import render
from django.views.generic import ListView

from cooking_recipes.recipes.models import Recipe


def landing_page(request):
    return render(request, 'common/landing_page.html')


class RecipesListView(ListView):
    template_name = 'common/recipes_all.html'
    model = Recipe
    category = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class MainDishesListView(RecipesListView):
    category = 'Main Dish'
    queryset = Recipe.objects.filter(recipe_type=category)


class SoupsListView(RecipesListView):
    category = 'Soup'
    queryset = Recipe.objects.filter(recipe_type=category)


class SaladsListView(RecipesListView):
    category = 'Salad'
    queryset = Recipe.objects.filter(recipe_type=category)


class DessertsListView(RecipesListView):
    category = 'Dessert'
    queryset = Recipe.objects.filter(recipe_type=category)
