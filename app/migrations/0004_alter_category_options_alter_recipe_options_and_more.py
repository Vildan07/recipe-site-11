# Generated by Django 5.0.3 on 2024-04-18 16:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_recipe_views'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['pk'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['pk'], 'verbose_name': 'Рецепт', 'verbose_name_plural': 'Рецепты'},
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Ингридиенты'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Публикация на сайте'),
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='users/')),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('site', models.URLField(blank=True, null=True)),
                ('github', models.CharField(blank=True, max_length=40, null=True)),
                ('telegram', models.CharField(blank=True, max_length=40, null=True)),
                ('instagram', models.CharField(blank=True, max_length=40, null=True)),
                ('facebook', models.CharField(blank=True, max_length=40, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]