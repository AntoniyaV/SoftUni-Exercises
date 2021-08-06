from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models


UserModel = get_user_model()


class Recipe(models.Model):
    MAIN_DISH = 'Main Dish'
    SOUP = 'Soup'
    SALAD = 'Salad'
    DESSERT = 'Dessert'
    recipe_category_choices =[
        (MAIN_DISH, 'Main Dish'),
        (SOUP, 'Soup'),
        (SALAD, 'Salad'),
        (DESSERT, 'Dessert'),
    ]

    recipe_type = models.CharField(
        max_length=10,
        choices=recipe_category_choices,
    )
    name = models.CharField(
        max_length=100,
    )
    ingredients = ArrayField(
        models.CharField(
            max_length=200,
        ),
    )
    instructions = models.TextField()
    image = models.ImageField(
        upload_to='recipes',
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
