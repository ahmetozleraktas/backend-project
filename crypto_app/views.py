from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .models import Crypto
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json
from django.views.decorators.cache import cache_page

_BASE_SYMBOL = 'USDT'
_API_KEY = '2fays/HuwDMPf6MDKchcTA==A0PchcFQX0LOAmQb'

@api_view(['POST', 'GET'])  # Specify the HTTP methods supported
@renderer_classes([JSONRenderer])  # Specify the renderers you want here
def index(request):
    return Response({'foo':'bar'})

    
@api_view(['POST', 'GET'])  # Specify the HTTP methods supported
@renderer_classes([JSONRenderer])  # Specify the renderers you want here
def price(request):
    if request.method == 'GET':
        symbol = request.GET.get('symbol', None)
        if symbol is None:
            return Response({'result':'NEED SYMBOL TO CREATE COLLECTION TASK.'})
        else:
            # add periodic task to django_celery_beat
            schedule, created = IntervalSchedule.objects.get_or_create(
                every=10,
                period=IntervalSchedule.SECONDS,
            )
            task, created = PeriodicTask.objects.get_or_create(
                interval=schedule,
                name=f'get_price_{symbol}',
                task='crypto_app.tasks.get_crypto_price',
                args=json.dumps([symbol]),
                kwargs=json.dumps({}),
            )
            return Response({'result':'PERIODIC TASK ADDED.'})
        

@api_view(['POST', 'GET'])  # Specify the HTTP methods supported
@renderer_classes([JSONRenderer])  # Specify the renderers you want here
@cache_page(60 * 15)
def show_price(request):
    if request.method == 'GET':
        symbol = request.GET.get('symbol', None)
        if symbol is None:
            return Response({'result':'NEED SYMBOL TO GET PRICE.'})
        else:
            try:
                # get all prices matching with symbol
                crypto = Crypto.objects.filter(symbol=symbol)
                # sort by timestamp
                crypto = crypto.order_by('timestamp')

                price_list = [price for price in crypto.values_list('price', flat=True)]
                
                return Response({f'result for {symbol}':price_list})
                
            except Crypto.DoesNotExist as e:
                print(e)
                return Response({'result':'NO PRICE FOUND.'})
            

@api_view(['POST', 'GET'])  # Specify the HTTP methods supported
@renderer_classes([JSONRenderer])  # Specify the renderers you want here
def coin_list(request):
    if request.method == 'GET':
        try:
            # get all unique symbols
            crypto = Crypto.objects.values_list('symbol', flat=True).distinct()
            return Response({'Coins in database':crypto})
        except Crypto.DoesNotExist as e:
            print(e)
            return Response({'result':'NO COINS FOUND.'})