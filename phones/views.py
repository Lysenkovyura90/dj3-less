from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    page_sort = request.GET.get("sort")
    all_phones = Phone.objects.all()
    if page_sort == 'min_price':
        all_phones = all_phones.order_by('price')
    elif page_sort == 'max_price':
        all_phones = all_phones.order_by('-price')
    elif page_sort == 'alpha':
        all_phones = all_phones.order_by('name')
    context = {
        'phones': all_phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
