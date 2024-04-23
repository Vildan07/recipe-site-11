from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Наименование рецепта', 'style': 'margin-top:10px'}),
                   'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Категория', 'style': 'margin-top: 10px'}),
                   'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Рецепт', 'style': 'margin-top: 10px'}),
                   'photo': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Фото', 'style': 'margin-top: 10px'}),
                   'published': forms.CheckboxInput(attrs={'class': 'form-check-input', 'placeholder': 'Публикация на сайте', 'style': 'margin-top:10px'})}


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'form2Example1'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'form2Example2'}))


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль повторно'}))

    class Meta:
        model = User
        fields = ('username', 'email')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        widgets = {'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text', 'rows': 5})}