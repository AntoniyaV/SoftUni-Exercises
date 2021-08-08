from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView, DetailView, UpdateView

from cooking_recipes.accounts.forms import SignUpForm, SignInForm, ProfileForm, UserForm
from cooking_recipes.accounts.models import RecipesUserProfile, RecipesUser
from cooking_recipes.recipes.models import Recipe

UserModel = get_user_model()


class SignUpView(CreateView):
    template_name = 'accounts/sign-up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('sign-in')


class SignInView(LoginView):
    template_name = 'accounts/sign-in.html'
    form_class = SignInForm

    def get_success_url(self):
        return reverse('landing')


# def sign_in(request):
#     if request.method == 'POST':
#         form = SignInForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('landing')
#
#     else:
#         form = SignInForm()
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'accounts/sign-in.html', context=context)


def sign_out(request):
    logout(request)
    return redirect('landing')


# class ProfileDetailsView(LoginRequiredMixin, FormView):
#     template_name = 'accounts/profile_details.html'
#     form_class = ProfileForm
#     success_url = reverse_lazy('profile')
#     profile_object = None
#
#     login_url = 'sign-in'
#
#     def get(self, request, *args, **kwargs):
#         self.profile_object = RecipesUserProfile.objects.get(pk=request.user.id)
#         return super().get(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         self.profile_object = RecipesUserProfile.objects.get(pk=request.user.id)
#         return super().post(request, *args, **kwargs)
#
#     def form_valid(self, form):
#         self.profile_object.profile_picture = form.cleaned_data['profile_picture']
#         self.profile_object.save()
#         return super().form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['recipes'] = Recipe.objects.filter(user_id=self.request.user.id)
#         context['profile'] = self.profile_object
#
#         return context

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
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'accounts/profile_edit.html', context=context)


# class ProfileEditView(UpdateView):
#     template_name = 'accounts/profile_edit.html'
#     model = RecipesUserProfile
#     fields = ('profile_picture',)
#     context_object_name = 'profile'
#     profile = None
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         profile = context['profile']
#         return context
#
#     def get_success_url(self):
#         pk = self.profile.user.id
#         return reverse('profile-details', kwargs={'pk': pk})