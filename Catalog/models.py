from django.db import models
from django.db.models import ImageField
from django.utils import timezone
from django.views.decorators.http import last_modified


class Task(models.Model):
    title = models.CharField("Название", max_length=50)
    task = models.TextField("Описание")

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="Наименование")
    description = models.CharField(max_length=100, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=20, verbose_name="Наименование")
    description = models.CharField(max_length=200, verbose_name="Описание")
    preview = models.ImageField(
        upload_to="products/foto",
        blank=True,
        null=True,
        verbose_name="Изображение(превью)",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
    )
    purchase_price = models.FloatField(
        verbose_name="Цена за покупку",
    )
    created_at = models.DateField(
        auto_now=True,
        verbose_name="Дата создания(записи в БД)",
    )
    updated_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата последнего изменения(записи в БД)",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "purchase_price", "category", "created_at"]
