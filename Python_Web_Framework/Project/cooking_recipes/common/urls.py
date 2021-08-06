from django.urls import path
from cooking_recipes.common import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('main-dishes/', views.MainDishesListView.as_view(), name='main-dishes'),
    path('soups/', views.SoupsListView.as_view(), name='soups'),
    path('salads/', views.SaladsListView.as_view(), name='salads'),
    path('desserts/', views.DessertsListView.as_view(), name='desserts'),
]