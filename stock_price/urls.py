from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('/stock_price/ ', views.stock_price, name='stock_price'),
    path('my-api/', views.stock_price, name='my-api'),
]