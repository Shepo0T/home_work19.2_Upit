from django.urls import path
from Catalog.apps import CatalogConfig
from Catalog.views import home, contacts
app_name = CatalogConfig.name

urlpatterns = [
    path('',home, name='home'),
    path('contacts/', contacts, name='contacts'),
]