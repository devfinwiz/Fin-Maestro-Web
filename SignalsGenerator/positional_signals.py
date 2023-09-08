import sys
import matplotlib
import yfinance as yf
import matplotlib as plt
sys.path.append("init")
from init import *

def signals_generator(ticker,num_of_signals):
    matplotlib.use('Agg')
    yf.pdr_override()
    plt.style.use('dark_background') #dark theme for plot

    #ticker = input()          #name of the stock for which signals are needed.
    #num_of_signals = 10      #number of buy/sell signals to be plotted

    df = yf.download(ticker)    #dataframe from yfinance for specific ticker

    closes = sorted(df.Close.tolist())
    low,high = closes[num_of_signals],closes[-num_of_signals]

    df['Signal'] = 0

    df.loc[df['Adj Close'] > high, 'Signal'] = -1
    df.loc[df['Adj Close'] < low, 'Signal'] = 1

    long = df.loc[df['Signal'] == 1]
    short = df.loc[df['Signal'] == -1]

    fig=plt.pyplot.figure()
    fig.set_figwidth(12)
    plt.pyplot.plot(df.index, df['Adj Close'],color='white', label='Close Price')
    plt.pyplot.plot(long.index, df.loc[long.index]['Adj Close'], '^', markersize=10, color='g', label='Long/Buy')
    plt.pyplot.plot(short.index, df.loc[short.index]['Adj Close'],'v', markersize=10, color='r', label='Short/Sell')
    plt.pyplot.ylabel('Closing Price')
    plt.pyplot.xlabel('Date')
    plt.pyplot.title(ticker)
    plt.pyplot.legend(loc='best')

    #plt.show()
    return fig


