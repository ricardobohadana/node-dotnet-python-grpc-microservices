import pandas as pd
from pandas_datareader.yahoo.headers import DEFAULT_HEADERS
import pandas_datareader.data as web
import datetime
import requests_cache

expire_after = datetime.timedelta(hours= 12)


def get_stock_price(ticker: str):
    session = requests_cache.CachedSession(cache_name='cache', backend='sqlite', expire_after=expire_after)
    session.headers = DEFAULT_HEADERS
    start = datetime.datetime(2022, 1, 1)
    end = datetime.datetime.now()
    try:
        df = web.DataReader(ticker, 'yahoo', start, end, session=session)
        latest_price = df.iloc[-1]['Adj Close']
        return {"ticker": ticker, "price": latest_price}
    except:
        return {"ticker": f"Erro, não foi possível encontrar o ticker {ticker}", "price": 0.0}

def get_stock_history_price(ticker: str):
    session = requests_cache.CachedSession(cache_name='cache', backend='sqlite', expire_after=expire_after)
    session.headers = DEFAULT_HEADERS
    start = datetime.datetime(2000, 1, 1)
    end = datetime.datetime.now()
    try:
        df = web.DataReader(ticker, 'yahoo', start, end, session=session)
        df.rename(columns = {'Adj Close':'AdjClose'}, inplace = True)
        df['Date'] = df.index
        df['Date'] = df['Date'].apply(lambda x: x.strftime('%m/%d/%Y'))
        df = df[['High', 'Low', 'Open', 'Close', 'Date']]
        data = df.to_dict(orient='records')
        return {"ticker": ticker, "data": data}
    except:
        return {"ticker": f"Erro, não foi possível encontrar o ticker {ticker}", "data": [{"High": 0.0, "Low": 0.0, "Open": 0.0, "Close": 0.0, "Date": "00/00/0000"}]}
    
# get_stock_history_price("AAPL");
## proto generate command:

# python -m grpc_tools.protoc -I. --python_out=../grpc_generated_files --grpc_python_out=../grpc_generated_files stock.proto