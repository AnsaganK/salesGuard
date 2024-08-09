from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse

from app.forms.client import ClientForm
from app.models import Client


@login_required
def client_list(request):
    clients = Client.objects.all().order_by('-created_at')
    return render(request, 'app/client/list.html', {
        'clients': clients
    })


@login_required
def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'app/client/detail.html', {
        'client': client
    })


@login_required
def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Клиент создан')
        else:
            messages.error(request, 'Ошибка при сохранении')
    return redirect(reverse('app:client_list'))


@login_required
def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    messages.success(request, 'Клиент удален')
    return redirect(reverse('app:client_list'))
