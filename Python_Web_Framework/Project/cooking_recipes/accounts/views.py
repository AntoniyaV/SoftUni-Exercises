from django.contrib.auth import get_user_model, login, logout
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from cooking_recipes.accounts.forms import SignUpForm, SignInForm

UserModel = get_user_model()


class SignUpView(CreateView):
    template_name = 'accounts/sign-up.html'
    model = UserModel
    form_class = SignUpForm
    success_url = reverse_lazy('sign-in')


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing')

    else:
        form = SignInForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/sign-in.html', context=context)


def sign_out(request):
    logout(request)
    return redirect('landing')


class ProfileDetailsView(FormView):
    template_name = 'accounts/profile.html'
