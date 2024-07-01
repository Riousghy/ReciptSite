from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField(default='')  # 设置默认值为空字符串
    instructions = models.TextField()

    def __str__(self):
        return self.name
