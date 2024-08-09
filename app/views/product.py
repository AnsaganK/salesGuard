from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse

from app.forms.product import ProductForm
from app.models import Product, Subcategory


@login_required
def create_product(request, pk):
    subcategory = get_object_or_404(Subcategory, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.subcategory = subcategory
            product.save()
            messages.success(request, 'Товар добавлен')
        else:
            messages.error(request, 'Ошибка')
    return redirect(reverse('app:product_list'))


@login_required
def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'app/product/list.html', {
        'products': products
    })


@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'app/product/detail.html', {
        'product': product
    })
