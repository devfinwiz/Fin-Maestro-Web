import talib
import csv
import pandas as pd

#---------------------------------------------------------------------------------------------
#returns a list of stock symbols from Tickers.csv

def get_symbols():
    flag=1
    comp=csv.reader(open("Prerequisites\Tickers.csv"))     
    tickers=[]
    
    for c in comp:
        if(flag==1):
            flag=0
            continue
        
        symbol=c[0]
        tickers.append(symbol)
        
    return tickers

#--------------------------------------------------------------------------------------------------
#returns a list of stocks that are trading over period SMA (close>period SMA)

def ma_above_scanner(period):
    tickers=get_symbols()
    stocks_over_sma=[]
    
    for symbol in tickers:
        try:
            df=pd.read_csv("Dataset\Resultant Dataset\\ticker_csvs\{}.csv".format(symbol))
            sma=talib.SMA(df['Close'],period)
            sma,close=list(sma)[-1],list(df['Close'])[-1]
            if(close>sma):
                stocks_over_sma.append(symbol)
        except:
            continue
        
    return stocks_over_sma

#--------------------------------------------------------------------------------------------------
#returns a list of stocks that are trading below period SMA (close<period SMA)

def ma_below_scanner(period):
    tickers=get_symbols()
    stocks_below_sma=[]
    
    for symbol in tickers:
        try:
            df=pd.read_csv("Dataset\Resultant Dataset\\ticker_csvs\{}.csv".format(symbol))
            sma=talib.SMA(df['Close'],period)
            sma,close=list(sma)[-1],list(df['Close'])[-1]
            if(close<sma):
                stocks_below_sma.append(symbol)
        except:
            continue
        
    return stocks_below_sma


            