from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {
    'blank': True,
    'null': True,
}


# Create your models here.
class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')

    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone_number = models.CharField(max_length=35, verbose_name="номер телефона", **NULLABLE)
    country = models.CharField(max_length=255, verbose_name="страна", **NULLABLE)

    # поля:
    # аватар,
    # номер телефона,
    # страна.

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
