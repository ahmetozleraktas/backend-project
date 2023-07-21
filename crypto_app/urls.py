from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('price/', views.price, name='price'),
    path('show-price/', views.show_price, name='show_price'),
]
