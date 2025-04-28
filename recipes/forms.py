from django import forms
from .models import Recipe, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'instructions', 'category', 'cooking_time', 'image']  # Add cooking_time here if not already included


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
