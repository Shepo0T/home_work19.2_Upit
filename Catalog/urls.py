from django.urls import path
from Catalog.apps import CatalogConfig
from Catalog.views import home,catalog, contacts, product

app_name = CatalogConfig.name

urlpatterns = [
    path('',home, name='home'),
    path('catalog',catalog, name='catalog'),
    path('contacts/',contacts, name='contacts'),
    path('product/<int:pk>',product, name='product')
]