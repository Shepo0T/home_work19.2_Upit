from django.urls import path
from Catalog.apps import CatalogConfig
from Catalog.views import HomeListView, ContactsView, CatalogListView, ProductDetailView, ProductUpdate, \
    ProductDeleteView, ProductCreateView, toggle_activity_product, ProductSaleView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('catalog', CatalogListView.as_view(), name='catalog'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('update_product/<int:pk>', ProductUpdate.as_view(), name='update_product'),
    path('delete_product/<int:pk>', ProductDeleteView.as_view(), name='delete'),
    path('create_product/', ProductCreateView.as_view(), name='create'),
    path('create_product_view/', ProductSaleView, name='create_product_view'),
    path('activity_product/<int:pk>/', toggle_activity_product, name='toggle_activity_product')
]
