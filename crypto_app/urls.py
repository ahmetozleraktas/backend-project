from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-coin/', views.price, name='price'),
    path('show-price/', views.show_price, name='show-price'),
    path('coin-list/', views.coin_list, name='coin-list'),
]
