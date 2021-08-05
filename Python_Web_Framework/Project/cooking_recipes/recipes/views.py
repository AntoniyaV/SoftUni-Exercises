from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from cooking_recipes.recipes.models import Recipe


def landing_page(request):
    return render(request, 'landing_page.html')


def recipe_create_warning(request):
    return render(request, 'recipe_create_warning.html')


class RecipeCreateView(CreateView):
    template_name = 'recipe_create.html'
    model = Recipe
    success_url = reverse_lazy('landing')
    fields = ('recipe_type', 'name', 'ingredients', 'instructions', 'image')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RecipeCreateView, self).form_valid(form)


class MainDishesListView(ListView):
    template_name = 'recipes_all.html'
    model = Recipe
    queryset = Recipe.objects.filter(recipe_type='main_dish')


class SoupsListView(ListView):
    template_name = 'recipes_all.html'
    model = Recipe
    queryset = Recipe.objects.filter(recipe_type='soup')


class SaladsListView(ListView):
    template_name = 'recipes_all.html'
    model = Recipe
    queryset = Recipe.objects.filter(recipe_type='salad')


class DessertsListView(ListView):
    template_name = 'recipes_all.html'
    model = Recipe
    queryset = Recipe.objects.filter(recipe_type='dessert')