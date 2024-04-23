from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', recipes_by_category, name='by_category'),
    path('recipe-detail/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('recipe-add/', recipe_create, name='recipe_create'),
    path('recipe-update/<int:pk>/', recipe_update, name='recipe_update'),
    path('recipe-delete/<int:pk>/', recipe_delete, name='recipe_delete'),
    path('category-detail/<int:pk>/', category_detail, name='category_detail'),
    path('add-category/', category_create, name='category_create'),
    path('update-category/<int:pk>/', category_update, name='category_update'),
    path('delete-category/<int:pk>/', category_delete, name='category_delete'),

    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),

    path('profile/<str:username>/', profile, name='profile'),
    path('save-comment/<int:pk>/', save_comment, name='save_comment'),
]