from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from cooking_recipes.accounts.models import RecipesUserProfile

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name',)


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = RecipesUserProfile
        fields = ('profile_picture',)