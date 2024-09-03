from django.shortcuts import render

from Catalog.models import Product


def home(request):
    return render(request, 'Catalog/home.html')


def catalog(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Главная'
    }
    return render(request, 'Catalog/catalog.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f' {name} ({phone}): {message})')
    return render(request, 'Catalog/contacts.html')


def product(request, pk):
    context = {
        'products': Product.objects.get(pk=pk)
    }

    return render(request, 'Catalog/product.html', context)
