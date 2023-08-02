from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-coin/', views.add_coin, name='add-coin'),
    path('show-price/', views.show_price, name='show-price'),
    path('coin-list/', views.coin_list, name='coin-list'),
    path('delete-coin/', views.delete_coin, name='delete-coin'),
]
