from django.core.exceptions import ValidationError


def recipe_category_validator(value):
    category_names = ['Main Dish', 'Soup', 'Salad', 'Dessert']
    if value not in category_names:
        raise ValidationError(f"Category must be one of the following: {', '. join(category_names)}")
