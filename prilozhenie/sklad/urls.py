from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tovar/', views.index_tovar, name='index_tovar'),
    path('priem/', views.TovarCreateView.as_view(), name='priem'),
    path('oformzak/', views.OrderCreateView.as_view(), name='oformzak'),
    path('add_client/', views.ClientCreateView.as_view(), name='add_client'),
    path('otgruzka/', views.otgruzka, name='otgruzka')
]