import matplotlib.pyplot as plt
import warnings
import yfinance as yf
import datetime as dt

warnings.filterwarnings("ignore")
yf.pdr_override()

plt.style.use('dark_background') #dark theme for plot

ticker ='ONMOBILE.NS'         #name of the stock for which signals are needed.
num_of_signals = 10      #number of buy/sell signals to be plotted

initial,end = dt.date.today() - dt.timedelta(days=900),dt.date.today()

df = yf.download(ticker,initial,end) #dataframe from yfinance for specific ticker

closes = sorted(df.Close.tolist())
low,high = closes[num_of_signals],closes[-num_of_signals]

df['Signal'] = 0

df.loc[df['Adj Close'] > high, 'Signal'] = -1
df.loc[df['Adj Close'] < low, 'Signal'] = 1

long = df.loc[df['Signal'] == 1]
short = df.loc[df['Signal'] == -1]

plt.figure(figsize=(16,8),num='Positional Signals')
plt.plot(df.index, df['Adj Close'],color='white', label='Close Price')
plt.plot(long.index, df.loc[long.index]['Adj Close'], '^', markersize=10, color='g', label='Long/Buy')
plt.plot(short.index, df.loc[short.index]['Adj Close'],'v', markersize=10, color='r', label='Short/Sell')
plt.ylabel('Closing Price')
plt.xlabel('Date')
plt.title(ticker)
plt.legend(loc='best')

plt.show()