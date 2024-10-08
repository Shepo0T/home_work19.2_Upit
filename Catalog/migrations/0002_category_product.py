# Generated by Django 5.1 on 2024-08-31 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length='20', verbose_name='Наименование')),
                ('description', models.TextField(max_length='100', verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length='20', verbose_name='Наименование')),
                ('description', models.TextField(max_length='200', verbose_name='Описание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='products/foto', verbose_name='Изображение(превью)')),
                ('purchase_price', models.FloatField(verbose_name='Цена за покупку')),
                ('created_at', models.DateField(verbose_name='Дата создания(записи в БД)')),
                ('updated_at', models.DateField(verbose_name='Дата последнего изменения(записи в БД)')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Catalog.category')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['name', 'updated_at', 'purchase_price', 'category', 'created_at'],
            },
        ),
    ]
