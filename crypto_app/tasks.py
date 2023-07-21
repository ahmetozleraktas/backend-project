from __future__ import absolute_import, unicode_literals

from celery import shared_task
import datetime
import requests
from .models import Crypto

_BASE_SYMBOL = 'USDT'
_API_URL = 'https://api.api-ninjas.com/v1/cryptoprice?symbol='
_API_KEY = '2fays/HuwDMPf6MDKchcTA==A0PchcFQX0LOAmQb'

@shared_task
def get_crypto_price(symbol: str):
    symbol = symbol + _BASE_SYMBOL
    api_url = _API_URL + symbol
    response = requests.get(api_url, headers={'X-Api-Key': _API_KEY})
    if response.status_code == requests.codes.ok:
        response = response.json()
        print(response)
        timestamp = datetime.fromtimestamp(response['timestamp'])
        crypto = Crypto(symbol=response['symbol'], price=float(response['price']), timestamp=timestamp)
        crypto.save()
        return True
    else:
        return False
