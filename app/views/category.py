from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect, reverse

from app.forms.category import CategoryForm, SubcategoryForm
from app.models.category import Subcategory, Category


@login_required
def create_subcategory(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            subcategory = form.save(commit=False)
            subcategory.category = category
            subcategory.save()
            messages.success(request, f'Подкатегория "{subcategory.name}" создана')
        else:
            messages.error(request, 'Ошибка при создании')
    return redirect(reverse('app:category_list'))


@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, f'Категория "{category.name}" создана')
        else:
            messages.error(request, 'Ошибка при создании')
    return redirect(reverse('app:category_list'))


@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'app/category/list.html', {
        'categories': categories
    })


@login_required
def subcategory_detail(request, slug):
    subcategory = get_object_or_404(Subcategory, slug=slug)
    products = subcategory.products.all().order_by('-created_at')
    return render(request, 'app/subcategory/detail.html', {
        'subcategory': subcategory,
        'products': products,
    })
