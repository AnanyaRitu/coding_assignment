from django.contrib import admin
from .models import CustomUser, Sales

admin.site.register(CustomUser)
admin.site.register(Sales)