from django.core.management import BaseCommand
import json

from Catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('catalog.json') as f:
            categories_list = json.load(f)
            return categories_list

    @staticmethod
    def json_read_products():
        with open('product.json') as f:
            product_list = json.load(f)
            return product_list

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(pk=category['pk'],
                         **category['fields'])
            )
        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(pk=product['pk'],
                        name=product['fields']['name'],
                        description=product['fields']['description'],
                        preview=product['fields']['preview'],
                        purchase_price=product['fields']['purchase_price'],
                        created_at=product['fields']['created_at'],
                        updated_at=product['fields']['updated_at'],
                        category=Category.objects.get(pk=product['fields']['category']))
            )
        Product.objects.bulk_create(product_for_create)