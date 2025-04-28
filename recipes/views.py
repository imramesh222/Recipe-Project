from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, Category
from .forms import RecipeForm, SignUpForm, CategoryForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def recipe_list(request):
    recipes = Recipe.objects.all()
    categories = Category.objects.all()

    query = request.GET.get('q')
    category_id = request.GET.get('category')

    if query:
        recipes = recipes.filter(Q(title__icontains=query) | Q(ingredients__icontains=query))

    if category_id:
        recipes = recipes.filter(category_id=category_id)

    return render(request, 'recipes/recipe_list.html', {'recipes': recipes, 'categories': categories})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user
            recipe.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})

@login_required
def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.created_by != request.user:
        return redirect('recipe_list')
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_form.html', {'form': form})

@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.created_by == request.user:
        recipe.delete()
    return redirect('recipe_list')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipe_list')
    else:
        form = SignUpForm()
    return render(request, 'recipes/signup.html', {'form': form})

# Category creation view
@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')  # Redirect to category list after successful creation
    else:
        form = CategoryForm()
    return render(request, 'recipes/category_form.html', {'form': form})

# Category list view
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'recipes/category_list.html', {'categories': categories})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')  # Adjust this if you have a different name
    return render(request, 'recipes/category_confirm_delete.html', {'category': category})