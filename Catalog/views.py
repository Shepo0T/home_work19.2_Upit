from gettext import Catalog

from django.shortcuts import render
from django.views.generic import ListView, View, DetailView

from Catalog.models import Product

class HomeListView(ListView):
    model = Product
    template_name = 'Catalog/home.html'

class ContactsView(View):
    def get(self,request,*args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f' {name} ({phone}): {message})')

        return render(request, 'Catalog/contacts.html')


class CatalogListView(ListView):
    model = Product
    template_name = 'Catalog/catalog.html'



class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


