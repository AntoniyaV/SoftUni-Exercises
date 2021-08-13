from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from cooking_recipes.recipes.models import Recipe


class RecipeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'recipe_create.html'
    model = Recipe
    success_url = reverse_lazy('landing')
    fields = ('recipe_type', 'name', 'ingredients', 'instructions', 'image')

    login_url = 'login-required'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RecipeDetailsView(DetailView):
    template_name = 'recipe_details.html'
    model = Recipe
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = context['recipe']

        is_owner = recipe.user == self.request.user
        context['is_owner'] = is_owner

        return context


class RecipeEditView(LoginRequiredMixin, UpdateView):
    template_name = 'recipe_edit.html'
    model = Recipe
    fields = ('recipe_type', 'name', 'ingredients', 'instructions', 'image')

    login_url = 'login-required'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('recipe-details', kwargs={'pk': pk})


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'recipe_delete.html'
    model = Recipe
    success_url = reverse_lazy('landing')
    login_url = 'login-required'
