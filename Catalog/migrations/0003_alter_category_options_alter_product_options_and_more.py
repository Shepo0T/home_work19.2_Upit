# Generated by Django 5.1 on 2024-09-02 18:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Catalog", "0002_category_product"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ["name"],
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name", "purchase_price", "category", "created_at"],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.CharField(max_length=100, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=20, verbose_name="Наименование"),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="Catalog.category",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateField(
                auto_now=True, verbose_name="Дата создания(записи в БД)"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.CharField(max_length=200, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=20, verbose_name="Наименование"),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateField(
                auto_now_add=True, verbose_name="Дата последнего изменения(записи в БД)"
            ),
        ),
    ]
