# Generated by Django 5.1 on 2024-09-27 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Catalog", "0006_alter_version_options_product_is_active"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": [
                    "name",
                    "purchase_price",
                    "category",
                    "created_at",
                    "is_active",
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]
