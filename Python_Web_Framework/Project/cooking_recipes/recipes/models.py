from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models

from cooking_recipes.recipes.validators import recipe_category_validator

UserModel = get_user_model()


class Recipe(models.Model):
    MAIN_DISH = 'Main Dish'
    SOUP = 'Soup'
    SALAD = 'Salad'
    DESSERT = 'Dessert'
    recipe_category_choices = [
        (MAIN_DISH, 'Main Dish'),
        (SOUP, 'Soup'),
        (SALAD, 'Salad'),
        (DESSERT, 'Dessert'),
    ]

    recipe_type = models.CharField(
        'Recipe Type',
        max_length=10,
        choices=recipe_category_choices,
        validators=[recipe_category_validator],
    )
    name = models.CharField(
        'Recipe Name',
        max_length=100,
    )
    ingredients = ArrayField(
        models.CharField(
            max_length=500,
        ),
        help_text='<small style="color:#168E16">*Please list your ingredients separated with a comma.</small>',
    )
    instructions = models.TextField()
    image = models.ImageField(
        upload_to='recipes',
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name}'
