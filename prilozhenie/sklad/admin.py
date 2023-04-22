from django.contrib import admin

from .models import Client, Tovar, Order

admin.site.register(Tovar)
admin.site.register(Client)
admin.site.register(Order)