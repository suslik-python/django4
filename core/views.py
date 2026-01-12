from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from .data import new_products

def main_page(request):

    search_query = request.GET.get('search')
    price_start = request.GET.get('price_start')
    price_end = request.GET.get('price_end')
    category = request.GET.get('category')

    if price_start == "": price_start = None
    if price_end == "": price_end = None

    if search_query != None:
        products = list(filter(
            lambda item: search_query.lower() in item['name'].lower(), 
            products
        ))

    if price_start is not None and price_end is None:
        products = list(filter(
            lambda item: item['price'] >= int(price_start),
            products
        ))

    if price_end is not None and price_start is None:
        products = list(filter(
            lambda item: item['price'] <= int(price_end),
            products
        ))

    if price_start is not None and price_end is not None:
        products = list(filter(
            lambda item: item['price'] >= int(price_start) and item['price'] <= int(price_end),
            products
        ))

    if category is not None:
        products = list(filter(
            lambda item: item['category'] == category, 
            products
        ))

    context = {
        'products': products
    }

    return render(request, 'index.html', context)

def create_products(request):
    if request.method == "POST":
        id = request.POST.get('id')
        name = request.POST.get('name')
        price = request.POST.get('price')
        category = request.POST.get('category')

        new_product = {
            'id': int(id),
            'name': name,
            'price': int(price),
            'category': category 
        }

        new_products.append(new_product)

        return redirect('main_page')
    else:
        return HttpResponseForbidden("Данный метод не разрешен")