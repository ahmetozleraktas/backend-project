import yfinance as yf
from datetime import datetime
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .models import Stock
import pandas as pd

@api_view(['POST', 'GET'])  # Specify the HTTP methods supported
@renderer_classes([JSONRenderer])  # Specify the renderers you want here
def index(request):
    return Response({'foo':'bar'})

    
@api_view(['POST', 'GET'])  # Specify the HTTP methods supported
@renderer_classes([JSONRenderer])  # Specify the renderers you want here
def stock_price(request):
    if request.method == 'GET':
        company_name = request.GET.get('company', None)
        if company_name is None:
            return Response({'result':'NONE'})
        company = yf.Ticker(company_name)
        # GET TODAYS DATE AND CONVERT IT TO A STRING WITH YYYY-MM-DD FORMAT (YFINANCE EXPECTS THAT FORMAT)
        end_date = datetime.now().strftime('%Y-%m-%d')
        company_hist = company.history(start='2023-07-01',end=end_date)
        print(type(company_hist))
        is_saved = save_df_to_db(company_hist, company_name)
        if is_saved is None:
            # print exist objects columns and values
            print(Stock.objects.filter(stock_name=company_name).values())

            return Response({'result':'EXISTS'})
        elif is_saved is True:
            return Response({'result':'SUCCESS'})
        else:
            return Response({'result':'FAILURE'})

    elif request.method == 'POST':
        # company_name = request.POST['company']
        company_name = request.data['company']
        end_date = datetime.now().strftime('%Y-%m-%d')
        company_hist = company.history(start='2023-07-01',end=end_date)
        is_saved = save_df_to_db(company_hist, company_name)
        if is_saved is None:
            return Response({'result':'EXISTS'})
        elif is_saved is True:
            return Response({'result':'SUCCESS'})
        else:
            return Response({'result':'FAILURE'})
    else:
        return Response({'foo':'bar'})
    

def save_df_to_db(df: pd.DataFrame, company_name: str):
    try:
    
        if Stock.objects.filter(stock_name=company_name).exists():
            return None
        else:
            for index, row in df.iterrows():
                stock = Stock(stock_name=company_name, open_price=row['Open'], close_price=row['Close'], high_price=row['High'], low_price=row['Low'], volume=row['Volume'], dividend=row['Dividends'], split=row['Stock Splits'], date=index)
                stock.save()
        return True
    except Exception as e:
        print(f"Error while saving dataframe: {e}.")
        return False