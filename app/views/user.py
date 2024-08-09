from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, reverse

from app.forms.profile import ProfileEditForm
from app.forms.user import UserCreateForm
from app.models import Profile


@login_required
def user_list(request):
    users = User.objects.all().order_by('-date_joined')
    roles = Profile.RoleChoices.choices
    return render(request, 'app/user/list.html', {
        'users': users,
        'roles': roles
    })


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'app/user/detail.html', {
        'user': user
    })


@login_required
def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if not form.is_valid():
            messages.error(request, 'Форма заполнена неправильно')
            return redirect(reverse('app:user_list'))

        user = form.save()
        profile = user.profile
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
    return redirect(reverse('app:user_list'))


@login_required
def change_user_status(request, username):
    user = get_object_or_404(User, username=username)
    user.is_active = not user.is_active
    user.save()
    if user.is_active:
        messages.success(request, 'Доступ открыт')
    else:
        messages.warning(request, 'Доступ закрыт')
    return redirect(reverse('app:user_list'))
