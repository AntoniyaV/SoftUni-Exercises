from django.contrib.auth import get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView

from cooking_recipes.accounts.forms import SignUpForm, ProfileForm, UserForm
from cooking_recipes.accounts.models import RecipesUserProfile
from cooking_recipes.recipes.models import Recipe

UserModel = get_user_model()


class SignUpView(CreateView):
    template_name = 'accounts/sign-up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('sign-in')


class SignInView(LoginView):
    template_name = 'accounts/sign-in.html'

    def get_success_url(self):
        return reverse('landing')


def sign_out(request):
    logout(request)
    return redirect('landing')


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/profile_details.html'
    model = RecipesUserProfile
    context_object_name = 'profile'

    login_url = 'login-required'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = context['profile']
        context['recipes'] = Recipe.objects.filter(user_id=profile.user.id)

        return context


@login_required(login_url='login-required')
def edit_profile(request, pk):
    user = UserModel.objects.get(pk=pk)
    profile = RecipesUserProfile.objects.get(pk=pk)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile-details', user.id)

    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    context = {
        'profile': profile,
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'accounts/profile_edit.html', context=context)

