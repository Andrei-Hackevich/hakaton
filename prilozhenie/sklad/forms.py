from django.forms import ModelForm

from .models import Order, Tovar, Client

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('client', 'tovar', 'amount')

class TovarForm(ModelForm):
    class Meta:
        model = Tovar
        fields = ('title', 'description', 'price', 'amount')

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ('title', 'adress', 'description', 'phone')