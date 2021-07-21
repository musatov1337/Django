from django.shortcuts import render

from mainapp.models import Product, ProductCategory


def index(request):
    title = 'Каталог'
    links_menu = [
        {'href': 'product_all', 'name': 'все'},
        {'href': 'product_home', 'name': 'дом'},
        {'href': 'product_office', 'name': 'офис'},
        {'href': 'product_modern', 'name': 'модерн'},
        {'href': 'product_classic', 'name': 'классик'},
    ]

    products = Product.objects.all()[:4]
    category = ProductCategory.objects.all()[:4]

    context = {
        'title' : title,
        'links_menu': links_menu,
        'related_products': products,
        'category': category,
    }
    return render(request, 'mainapp/products.html', context)