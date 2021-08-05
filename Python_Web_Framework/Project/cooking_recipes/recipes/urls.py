from django.contrib.auth.decorators import login_required
from django.urls import path
from cooking_recipes.recipes import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('login-required/', views.recipe_create_warning, name='login-required'),
    path('create-recipe/', login_required(views.RecipeCreateView.as_view(), login_url='login-required'), name='create-recipe'),
    path('main-dishes/', views.MainDishesListView.as_view(), name='main-dishes'),
    path('soups/', views.SoupsListView.as_view(), name='soups'),
    path('salads/', views.SaladsListView.as_view(), name='salads'),
    path('desserts/', views.DessertsListView.as_view(), name='desserts'),
]