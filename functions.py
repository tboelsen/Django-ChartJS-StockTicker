import pandas as pd
import numpy as np
import yfinance as yf
import pandas_datareader.nasdaq_trader as nsdq
from datetime import datetime, timedelta

#get a list of S&P500 tickers
def get_sp():
    table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    df = table[0]
    df['output'] = df[['Symbol', 'Security']].agg(' - '.join, axis=1)
    return df['output'].tolist()

#get historical stock data from Yahoo
def get_stock_data(start, end, ticker):
    stock = yf.download(ticker, progress=False, actions='inline', start=start, end=end)
    return stock
