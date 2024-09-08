from django.urls import path
from Catalog.apps import CatalogConfig
from Catalog.views import HomeListView, ContactsView, CatalogListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('',HomeListView.as_view(), name='home'),
    path('catalog',CatalogListView.as_view(), name='catalog'),
    path('contacts/',ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>',ProductDetailView.as_view(), name='product')
]