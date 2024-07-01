from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('recipes/', views.all_recipes, name='all_recipes'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
]
