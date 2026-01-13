from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/inventory.html', {'products': products})


def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        description = request.POST.get('description', '')
        image = request.FILES.get('image')

        product = Product.create_product(
            name=name,
            price=price,
            stock=int(stock),
            description=description
        )

        if image:
            product.image = image
            product.save()

        return redirect('inventory')

    return render(request, 'inventory/product_form.html')


def product_edit(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.stock = int(request.POST.get('stock'))
        product.description = request.POST.get('description', '')

        image = request.FILES.get('image')
        if image:
            product.image = image

        product.save()
        return redirect('inventory')

    return render(request, 'inventory/product_form.html', {'product': product})


def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product_name = product.name
    product.delete()
    messages.success(request, f'"{product_name}" was deleted successfully!')
    return redirect('inventory')
