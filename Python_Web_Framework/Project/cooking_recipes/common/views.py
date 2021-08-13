from django.shortcuts import render
from django.views.generic import ListView

from cooking_recipes.recipes.models import Recipe


def landing_page(request):
    return render(request, 'common/landing_page.html')


def sign_in_warning(request):
    return render(request, 'common/sign_in_warning.html')


class RecipesListView(ListView):
    template_name = 'common/recipes_all.html'
    model = Recipe
    category = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class MainDishesListView(RecipesListView):
    category = Recipe.MAIN_DISH
    queryset = Recipe.objects.filter(recipe_type=category)


class SoupsListView(RecipesListView):
    category = Recipe.SOUP
    queryset = Recipe.objects.filter(recipe_type=category)


class SaladsListView(RecipesListView):
    category = Recipe.SALAD
    queryset = Recipe.objects.filter(recipe_type=category)


class DessertsListView(RecipesListView):
    category = Recipe.DESSERT
    queryset = Recipe.objects.filter(recipe_type=category)
