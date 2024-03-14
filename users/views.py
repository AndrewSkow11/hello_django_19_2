from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import UserForgotPasswordForm, UserSetNewPasswordForm
from django.views.generic import CreateView, View, TemplateView

from config import settings
from users.forms import UserForm
from users.models import User


# Create your views here.
class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Успешно',
            message='________________',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email],
        )
        print("Письмо после регистрации отправлено")
        return super().form_valid(form)


class UserForgotPasswordView(SuccessMessageMixin, PasswordResetView):
    """
    Представление по сбросу пароля по почте
    """
    form_class = UserForgotPasswordForm
    template_name = 'users/user_password_reset.html'
    success_url = reverse_lazy('home')
    success_message = 'Письмо с инструкцией по восстановлению пароля отправлена на ваш email'
    subject_template_name = 'system/email/password_subject_reset_mail.txt'
    email_template_name = 'system/email/password_reset_mail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Запрос на восстановление пароля'
        return context


class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    """
    Представление установки нового пароля
    """
    form_class = UserSetNewPasswordForm
    template_name = 'users/user_password_set_new.html'
    success_url = reverse_lazy('home')
    success_message = 'Пароль успешно изменен. Можете авторизоваться на сайте.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Установить новый пароль'
        return context
