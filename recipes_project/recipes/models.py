from django.db import models
from django.contrib.auth.models import User

# Модель для категории
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)  # Заголовок рецепта
    description = models.TextField()  # Описание рецепта
    instructions = models.TextField(default='')  # Инструкция
    cooking_time = models.IntegerField(help_text="Время в минутах")  # Время приготовления
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)  # Изображение рецепта
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Автор рецепта
    categories = models.ManyToManyField(Category)  # Категории рецепта
    steps = models.TextField()  # Этапы приготовления
    ingredients = models.TextField(default='')  # Ингредиенты рецепта

    def __str__(self):
        return self.title