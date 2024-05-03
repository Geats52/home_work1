from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

from .models import Client, Product, Order
from .forms import ClientForm, ProductForm, ProductCreateForm

from datetime import timedelta
import logging

def index(request):
    return render(request, 'index.html')


def create_client_view(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_clients')  
    else:
        form = ClientForm()
    return render(request, 'create_client.html', {'form': form})


def all_clients_view(request):
    clients = Client.objects.all()
    return render(request, 'all_clients.html', {'clients': clients})


def update_client_view(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('all_clients')  
    else:
        form = ClientForm(instance=client)
    return render(request, 'update_client.html', {'form': form, 'client': client})


def delete_client_view(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('all_clients') 
    return render(request, 'delete_client.html', {'client': client})



def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_products')  
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})


def all_products(request):
    products = Product.objects.all()
    return render(request, 'all_products.html', {'products': products})

def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('all_products')  
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form, 'product': product})



def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('all_products') 
    return render(request, 'delete_product.html', {'product': product})



def orders(request):
    orders = Order.objects.all()
    return HttpResponse(orders)

def get_orders_by_client(request):
    if request.method == 'POST':
        client_id = request.POST.get('client_id')
        period = request.POST.get('period')
        unique = request.POST.get('unique')
        kwargs = {'client_id': client_id}
        if period:
            kwargs['period'] = period
        if unique:
            kwargs['unique'] = unique
        return HttpResponseRedirect(reverse('all_client_orders', kwargs=kwargs))
    return render(request, 'get_client_orders.html')


def all_client_orders(request, **kwargs):
    client_id = kwargs.get('client_id')
    period = kwargs.get('period')
    unique = kwargs.get('unique')
    client = get_object_or_404(Client, pk=client_id)
    if period:
        end_date = timezone.now()
        start_date = end_date - timedelta(days=int(period))
        orders = Order.objects.filter(client=client, order_date__gte=start_date, order_date__lte=end_date)
    else:
        orders = Order.objects.filter(client=client)
    if unique:
        products = Product.objects.filter(order__in=orders).distinct()
    else:
        products = Product.objects.filter(order__in=orders)
    return render(request, 'all_client_orders.html',
                  {'unique': unique, 'period': period, 'client': client, 'orders': orders, 'products': products})



def get_products_by_id(request, success_message=None):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        return redirect(reverse('products_update', args=(product_id,)))
    return render(request, 'products_update.html', {'success_message': success_message})

def products_update(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            success_message = f"Товар с ID {product_id} успешно обновлён."
            return redirect('get_products_by_id', success_message=success_message)
    else:
        form = ProductForm(instance=product)
    return render(request, 'products.html', {'form': form})

def products_create(request):
    success_message = None
    if request.method == 'POST':
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            photo = request.FILES.get('photo')
            if photo:
                new_product = Product(name=name, description=description, price=price, quantity=quantity, photo=photo)
            else:
                new_product = Product(name=name, description=description, price=price, quantity=quantity)
            new_product.save()
            if photo:
                fs = FileSystemStorage()
                fs.save('product_photos/' + photo.name, photo)
            success_message = f"Product successfully created with ID: {new_product.pk}."


