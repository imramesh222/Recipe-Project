from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/add/', views.recipe_create, name='recipe_create'),
    path('recipe/<int:pk>/edit/', views.recipe_edit, name='recipe_edit'),
    path('recipe/<int:pk>/delete/', views.recipe_delete, name='recipe_delete'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='recipes/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('categories/', views.category_list, name='category_list'),
    path('category/add/', views.category_create, name='category_create'),  # Add this line
    path('category/<int:pk>/delete/', views.category_delete, name='category_delete'),

]
