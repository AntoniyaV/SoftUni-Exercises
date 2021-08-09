from django.urls import path
from cooking_recipes.recipes import views

urlpatterns = [
    path('create-recipe/', views.RecipeCreateView.as_view(), name='recipe-create'),
    path('details/<int:pk>', views.RecipeDetailsView.as_view(), name='recipe-details'),
    path('edit/<int:pk>', views.RecipeEditView.as_view(), name='recipe-edit'),
    path('delete/<int:pk>', views.RecipeDeleteView.as_view(), name='recipe-delete'),
]