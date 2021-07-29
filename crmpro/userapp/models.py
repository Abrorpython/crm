from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from .managers import CustomUserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    # These fields tie to the roles!
    ADMIN = 1
    KASSIR = 2
    SOTUVCHI = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (KASSIR, 'Kassir'),
        (SOTUVCHI, 'Sotuvchi')
    )
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
