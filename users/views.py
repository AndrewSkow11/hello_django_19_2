from django.shortcuts import render
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core.mail import send_mail

from django.views.generic import CreateView, View, TemplateView
# from django.urls import reverse_lazy
# from django.contrib.auth.tokens import default_token_generator
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes
# from django.contrib.sites.models import Site
# from django.core.mail import send_mail
# from django.shortcuts import redirect
# from django.contrib.auth import login
# from django.contrib.auth import get_user_model

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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Регистрация на сайте'
    #     return context
    #
    # def form_valid(self, form):
    #     user = form.save(commit=False)
    #     user.is_active = False
    #     user.save()
    #     # Функционал для отправки письма и генерации токена
    #     token = default_token_generator.make_token(user)
    #     uid = urlsafe_base64_encode(force_bytes(user.pk))
    #     activation_url = reverse_lazy('confirm_email', kwargs={'uidb64': uid, 'token': token})
    #     current_site = Site.objects.get_current().domain
    #     send_mail(
    #         'Подтвердите свой электронный адрес',
    #         f'Пожалуйста, перейдите по следующей ссылке, чтобы подтвердить свой адрес электронной почты: http://{current_site}{activation_url}',
    #         'service.notehunter@gmail.com',
    #         [user.email],
    #         fail_silently=False,
    #     )
    #     return redirect('email_confirmation_sent')

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Регистрация в магазине',
            message='Вы зарегестрировались на нашей платформе',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email],
        )
        print("Письмо после регистрации отправлено")
        return super().form_valid(form)
