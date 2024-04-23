from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    search_fields = ('title',)
    list_filter = ('title',)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created', 'published', 'get_photo')
    list_display_links = ('name', 'category')
    search_fields = ('name', 'category')
    list_filter = ('category', 'published')
    list_editable = ('published',)

    def get_photo(self, recipe):
        if recipe.photo:
            photo_url = recipe.photo.url
        else:
            photo_url = 'https://miro.medium.com/v2/resize:fit:1200/1*2z1QXCJntlNnqPRYylbpmg.jpeg'
        return mark_safe(f'<img src="{photo_url}" width="75px">')

    get_photo.short_description = 'Фото'



admin.site.register(Category)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(CustomUser)
