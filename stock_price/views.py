import yfinance as yf
from datetime import datetime
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

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
        company_hist = company.history(start='2022-01-01',end=end_date)
        
        # return the data but not to the template
        return Response(company_hist.to_json())

    elif request.method == 'POST':
        # company_name = request.POST['company']
        company_name = request.data['company']
        company = yf.Ticker(company_name)
        # GET TODAYS DATE AND CONVERT IT TO A STRING WITH YYYY-MM-DD FORMAT (YFINANCE EXPECTS THAT FORMAT)
        end_date = datetime.now().strftime('%Y-%m-%d')
        company_hist = company.history(start='2022-01-01',end=end_date)
        
        # return the data but not to the template
        return Response(company_hist.to_json())
    else:
        return Response({'foo':'bar'})