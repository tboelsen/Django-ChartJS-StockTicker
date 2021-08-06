from django.shortcuts import render

import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime

from .functions import get_stock_data, get_sp

start = datetime(2011,1,1)
end = datetime.today()

def IndexView(request):

    tickers = get_sp()

    #for default start page
    ticker = 'CVX - Chevron Corp.'
    tic = 'CVX'
    stockdata = get_stock_data(start, end, tic)
    index = stockdata.index.astype(str).tolist()
    prices = stockdata['Adj Close'].tolist()

    #update data once the user selects a new ticker
    if request.method == 'POST':
        ticker = request.POST['ticker']
        tic = ticker.split(' ', 1)[0]
        stockdata = get_stock_data(start, end, tic)
        index = stockdata.index.astype(str).tolist()
        prices = stockdata['Adj Close'].tolist()
        context = {'tickers': tickers, 'ticker':ticker, 'tic':tic, 'index': index, 'prices': prices}
        return render(request, 'index.html', context)

    #initial return when first opening the site
    context = {'tickers': tickers, 'ticker':ticker, 'tic': tic, 'index': index, 'prices': prices}
    return render(request, 'index.html', context)
