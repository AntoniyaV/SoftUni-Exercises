from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from cooking_recipes.accounts.manager import RecipesUserManager


class RecipesUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )
    first_name = models.CharField(
        max_length=30,
        blank=True,
    )
    last_name = models.CharField(
        max_length=30,
        blank=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'

    objects = RecipesUserManager()

    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        if full_name == ' ':
            return None
        return full_name


class RecipesUserProfile(models.Model):
    profile_picture = models.ImageField(
        upload_to='profiles',
        blank=True,
    )
    user = models.OneToOneField(
        RecipesUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

from cooking_recipes.accounts.signals import *
