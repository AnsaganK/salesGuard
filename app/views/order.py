import pdfkit
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.template.loader import get_template
from pytils.translit import slugify

from app.forms.order import OrderForm
from app.models import Product, Order, Client
from constants import PATH_WKHTMLTOPDF


def order_list(request):
    orders = Order.objects.all()
    orders = orders.select_related('product')
    orders = orders.select_related('client')
    return render(request, 'app/order/list.html', {
        'orders': orders
    })


@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.created_user = request.user
            order.save()
            messages.success(request, f'Заказ №{order.id} создан')
        else:
            print(form.errors)
            messages.error(request, 'Ошибка')
        return redirect(reverse('app:order_list'))
    clients = Client.objects.all()
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'app/order/create.html', {
        'products': products,
        'clients': clients
    })


@login_required
def delete_order(request, uuid):
    order = get_object_or_404(Order, uuid=uuid)
    order.delete()
    messages.success(request, 'Заказ успешно удален')
    return redirect(reverse('app:order_list'))


@login_required
def order_check(request, uuid):
    order = get_object_or_404(Order, uuid=uuid)
    return None


@login_required
def order_check_pdf(request, uuid):
    order = get_object_or_404(Order, uuid=uuid)
    template = get_template('app/order/pdf.html')
    html = template.render({
        'order': order,
    })
    options = {
        'margin-top': '0.3cm',
        'margin-right': '1.0cm',
        'margin-bottom': '0.0cm',
        'margin-left': '1.0cm',
        'page-size': 'A6',
        'copies': 1,
        # 'dpi': 96
    }

    config = pdfkit.configuration(wkhtmltopdf=PATH_WKHTMLTOPDF) if PATH_WKHTMLTOPDF else None

    pdf = pdfkit.from_string(html, False, options, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment;filename = "Order #{order.id}.pdf"'
    return response
