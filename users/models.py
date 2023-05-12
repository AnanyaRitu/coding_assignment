from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class Sales(models.Model):
    id=models.IntegerField(default=1,unique=True,primary_key=True)
    order_id=models.CharField(max_length=255, unique=True)
    order_date=models.DateTimeField()
    ship_date=models.DateTimeField()
    ship_mode=models.CharField(max_length=255)
    customer_id=models.CharField(max_length=255)
    customer_name=models.CharField(max_length=255)
    segment=models.CharField(max_length=255)
    country=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    postal_code=models.CharField(max_length=255)
    region=models.CharField(max_length=255)
    product_id=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    sub_category=models.CharField(max_length=255)
    product_name=models.TextField()
    sales=models.FloatField()

    def __str__(self):
        return self.order_id




