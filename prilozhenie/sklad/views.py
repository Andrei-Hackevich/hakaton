from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import Order, Tovar, Client
from .forms import OrderForm, TovarForm, ClientForm


def index_tovar(request):
    tovars = Tovar.objects.all()
    context = {'tovars': tovars}
    return render(request, 'index_tovar.html', context=context)


def index(request):
    return render(request, 'auto2.html')


def otgruzka(request):
    try:
        order = Order.objects.all()
        for order in orders:
            amount = Tovar.objects.all().values('tovar__amount')
            if amount > order.amount:
                context = {'order': order}
    except Exception as e:
        return HttpResponse('Заказов нет')
    else:
        return render(request, 'otgruzka.html', context=context)


class TovarCreateView(CreateView):
    template_name = 'priem.html'
    form_class = TovarForm
    success_url = reverse_lazy('index')


class ClientCreateView(CreateView):
    template_name = 'add_client.html'
    form_class = ClientForm
    success_url = reverse_lazy('index')


class OrderCreateView(CreateView):
    template_name = 'oformzak.html'
    form_class = OrderForm
    success_url = reverse_lazy('index')
