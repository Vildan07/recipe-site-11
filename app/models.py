from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="Категория")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["pk"]


class Recipe(models.Model):
    name = models.CharField(max_length=100, verbose_name="Рецепт")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    content = models.TextField(verbose_name="Ингридиенты", blank=True, null=True)
    photo = models.ImageField(upload_to="photos/", verbose_name="Фото", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    published = models.BooleanField(default=True, verbose_name="Публикация на сайте")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
        ordering = ["pk"]

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="users/", null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    site = models.URLField(null=True, blank=True)
    github = models.CharField(max_length=40, null=True, blank=True)
    telegram = models.CharField(max_length=40, null=True, blank=True)
    instagram = models.CharField(max_length=40, null=True, blank=True)
    facebook = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["-pk"]


class Comment(models.Model):
    text = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    commentator = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Пользователь: {self.commentator.username}\nКоментарий: {self.text}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-pk"]

