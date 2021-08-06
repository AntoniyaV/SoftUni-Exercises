from django.urls import path
from cooking_recipes.accounts import views

urlpatterns = [
    path('sign-up/', views.SignUpView.as_view(), name='sign-up'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-out/', views.sign_out, name='sign-out'),
    path('profile/', views.ProfileDetailsView.as_view(), name='profile')
]