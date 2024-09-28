from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, View, DetailView, UpdateView, DeleteView, CreateView
from pytils.translit import slugify

from Catalog.forms import ProductForm, VersionForm
from Catalog.models import Product, Version


class MyLoginRequiredMixin(LoginRequiredMixin):

    login_url = 'users:login'
    redirect_field_name = "redirect_to"

class HomeListView(ListView):
    model = Product
    template_name = 'Catalog/home.html'


class ContactsView(View):
    def get(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f' {name} ({phone}): {message})')

        return render(request, 'Catalog/contacts.html')


class CatalogListView( ListView):
    model = Product
    template_name = 'Catalog/catalog.html'


class ProductDetailView(MyLoginRequiredMixin, DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class ProductUpdate(MyLoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('Catalog:product', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(MyLoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('Catalog:catalog')


class ProductCreateView(MyLoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('Catalog:catalog')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()

        return super().form_valid(form)




def CreateProductView(request):
    product_list = Product.objects.all()
    context = {
        'object_product': product_list,

    }

    return render(request, 'Catalog/create_products_view.html', context)


def toggle_activity_product(request, pk):
    Product_item = get_object_or_404(Product, pk=pk)
    if Product_item.is_active:
        Product_item.is_active = False
    else:
        Product_item.is_active = True

    Product_item.save()

    return redirect(reverse('Catalog:catalog'))



