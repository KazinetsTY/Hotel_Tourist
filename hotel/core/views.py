from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, UpdateView

from core.forms import UserCreationForm, UserUpdateForm, RoleCreationForm, UserRegisterForm
from core.models import User

from core.const import PAGE_SIZE
from user_role.models import Role




class IndexView(TemplateView):
    template_name = "base.html"


class UserListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "core.view_users"
    context_object_name = "users"
    template_name = "core/users/list.html"
    model = User
    paginate_by = PAGE_SIZE


class UserCreateView(PermissionRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = "core.add_users"
    form_class = UserCreationForm
    template_name = "core/users/create.html"
    success_url = reverse_lazy("core:users_list")
    success_message = "Пользователь успешно создан"


class UserUpdateView(PermissionRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = "core.change_users"
    form_class = UserUpdateForm
    model = User
    template_name = "core/users/update.html"
    success_url = reverse_lazy("core:users_list")
    success_message = "Пользователь успешно обновлен"


class RoleListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "user_role.view_role"
    context_object_name = "roles"
    template_name = "core/roles/list.html"
    model = Role
    paginate_by = PAGE_SIZE


class RoleCreateView(PermissionRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = "user_role.add_role"
    form_class = RoleCreationForm
    template_name = "core/roles/create.html"
    success_url = reverse_lazy("core:role_list")
    success_message = "Роль успешно создана"


class RoleUpdateView(
    PermissionRequiredMixin,
    LoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView
):
    permission_required = "user_role.change_role"
    form_class = RoleCreationForm
    model = Role
    template_name = "core/roles/update.html"
    success_url = reverse_lazy("core:role_list")
    success_message = "Роль успешно обновлена"


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Пользователь успешно создан')
            return redirect('core:login')
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form': form})


