from django.shortcuts import render


def index(request):
    context = {
        'slogan': 'акции'
    }
    return render(request, 'geekshop/index.html', context)


def contact(request):
    return render(request, 'geekshop/contact.html')