from django.contrib import admin
from .models import Category, Recipe

# Register the Category model
admin.site.register(Category)
admin.site.register(Recipe)
