from django.urls import path
from cooking_recipes.accounts import views

urlpatterns = [
    path('sign-up/', views.SignUpView.as_view(), name='sign-up'),
    path('sign-in/', views.SignInView.as_view(), name='sign-in'),
    path('sign-out/', views.sign_out, name='sign-out'),
    path('profile/<int:pk>', views.ProfileDetailsView.as_view(), name='profile-details'),
    path('profile/edit/<int:pk>', views.edit_profile, name='profile-edit'),
]