from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from .forms import *

# Create your views here.


def index(request):
    # categories = Category.objects.all()
    recipes = Recipe.objects.all()
    context = {
        # 'categories': categories,
        'recipes': recipes,
        'title': "Главное меню"
    }
    return render(request, 'app/index.html', context=context)


def recipes_by_category(request, category_id):
    recipes = Recipe.objects.filter(category_id=category_id)
    # categories = Category.objects.all()
    context = {
        'recipes': recipes,
        # 'categories': categories,
        'title': "Основное меню по категориям"

    }
    return render(request, 'app/index.html', context=context)


"""
Bu yerdan boshlab reseptlarga bog'liq funksiyalar yozilgan!
"""


@permission_required('app.view_recipe', login_url='index')
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    comments = Comment.objects.filter(recipe_id=recipe.pk)
    context = {
        'recipe': recipe,
        'form': CommentForm(),
        'comments': comments,
    }
    return render(request, 'app/recipe_detail.html', context=context)


@permission_required('app.add_recipe', login_url='index')
def recipe_create(request):

    form = RecipeForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        recipe = form.save(commit=False)
        recipe.author = request.user
        recipe.save()
        messages.success(request, f"Рецепт: {recipe.name}. Успешно добавлен на сайт! ")
        return redirect('index')

    form = RecipeForm()
    context = {
        'form': form,
    }
    return render(request, 'app/recipe_form.html', context=context)


@permission_required('app.change_recipe', login_url='index')
def recipe_update(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.user == recipe.author:

        form = RecipeForm(data=request.POST or None, instance=recipe, files=request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'app/recipe_form.html', {'form': form})
    else:
        return HttpResponse("У вас нет прав на изменение рецептов!!!")

@permission_required('app.delete_recipe', login_url='index')
def recipe_delete(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {
        'recipe': recipe,
        'title': 'Удаление рецепта'
    }
    if request.method == 'POST':
        recipe.delete()
        return redirect('index')
    return render(request, 'app/recipe_delete.html', context=context)


"""
BU yerdan boshlanib Categoryalar uchun viewlar yozilgan!
"""


@permission_required('app.view_category', login_url='index')
def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    context = {
        'category': category
    }
    return render(request, 'app/category_detail.html', context=context)


@permission_required('app.add_category', login_url='index')
def category_create(request):
    form = CategoryForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')

    form = CategoryForm()
    context = {
        'form': form
    }
    return render(request, 'app/category_form.html', context)


@permission_required('app.change_category', login_url='index')
def category_update(request, pk):
    category = Category.objects.get(pk=pk)
    form = CategoryForm(data=request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'app/category_form.html', {'form': form})


@permission_required('app.delete_category', login_url='index')
def category_delete(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('index')
    return render(request, 'app/category_delete.html', {'category': category})


"""
Bu yerdan boshlanib Login, Logout, Register lar uchun viewlar yozilgan!
"""


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"{user.username.title()} добро пожаловать на сайт!")
            return redirect('index')

        if form.errors:
            for error in form.error_messages.values():
                messages.error(request, f"{error}")

    form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'app/login.html', context=context)


def user_logout(request):
    logout(request)
    messages.warning(request, "Вы покинули сайт!")
    return redirect('login')


def user_register(request):
    form = RegisterForm(data=request.POST)
    if form.is_valid():
        user = form.save()
        messages.success(request, f"{user.username.title()} введите имя пользователя, пароль и ввойдите на сайт!")
        return redirect('login')

    form = RegisterForm()
    context = {
        'form': form,
        'title': 'Регистрация'
    }
    return render(request, 'app/register.html', context=context)


def profile(request, username):
    if request.user.username == username or request.user.is_superuser:
        user = User.objects.get(username=username)
        recipes= Recipe.objects.filter(author=user)
        context = {
            'user': user,
            'title': f'Страница пользователя {user.username}',
            'recipes': recipes
        }
        try:
            custom_user = CustomUser.objects.get(user=user)
            context['custom_user'] = custom_user

        except:
            pass
        return render(request, "app/profile.html", context=context)
    return HttpResponse("Страниица не найдена")


def save_comment(request, pk):
    if request.method == "POST":
        recipe = Recipe.objects.get(pk=pk)
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.commentator = request.user
            comment.save()
            messages.success(request, f"Комментарий успешно добавлен! Комментарий добавил(а) пользователь: {request.user.username}")
            return redirect('recipe_detail', pk=pk)
    return HttpResponse("Страница не найдена!")
