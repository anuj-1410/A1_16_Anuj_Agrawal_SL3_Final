from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    form = ProductForm()
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('product_list')
    
    context = {
        'products': products,
        'form': form
    }
    return render(request, 'inventory/product_list.html', context)