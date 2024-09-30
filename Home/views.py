from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product, Category
from django.contrib import messages

def home(request):
    products = Product.objects.all()
    return render(request, 'Home/index.html', {'products': products})

def add_product(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST.get('product_name')
        description = request.POST.get('product_description')
        category_id = request.POST.get('product_category')
        product_image = request.FILES.get('product_image')
        
        # get object use to null run without error
        
        my_category = get_object_or_404(Category, id=category_id)
        Product.objects.create(name=name, description=description, product_image=product_image, category=my_category)
        # product adedd message alert
        messages.success(request, 'Product added successfully')
        return redirect('Home')
    return render(request, 'Home/add_product.html', {'categories': categories})

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()

    if request.method == 'POST':
        product.name = request.POST.get('product_name')
        product.description = request.POST.get('product_description')
        product_image = request.FILES.get('product_image')
        if product_image:
              product.product_image = product_image
        category_id = request.POST.get('product_category')
        product.category = get_object_or_404(Category, id=category_id)
        product.save()
        messages.success(request, 'Product updated successfully')
        return redirect('Home')
    return render(request, 'Home/edit_product.html',{'products' :product ,'categories': categories})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully')
        return redirect('Home')
    return render(request, 'Home/confirm_deletation.html', {'product': product})
# there is no products its product

