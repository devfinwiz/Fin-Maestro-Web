from backtesting import Backtest, Strategy
from typing import Sequence
from backtesting.test import SMA
import pandas as pd
from numbers import Number
from nsepy import get_history
from datetime import date
import yfinance as yf


def crossover(series1: Sequence, series2: Sequence) -> bool:
        """
        Return `True` if `series1` just crossed over (above)
        `series2`.

            >>> crossover(self.data.Close, self.sma)
            True
        """
        series1 = (
            series1.values if isinstance(series1, pd.Series) else
            (series1, series1) if isinstance(series1, Number) else
            series1)
        series2 = (
            series2.values if isinstance(series2, pd.Series) else
            (series2, series2) if isinstance(series2, Number) else
            series2)
        try:
            return series1[-2] < series2[-2] and series1[-1] > series2[-1]
        except IndexError:
            return False
        
class SmaCross(Strategy):
    def init(self):
        price = self.data.Close
        sma1=10#int(input("First moving avergae: "))
        sma2=20#int(input("Second moving average: "))
        self.ma1 = self.I(SMA, price, sma1)
        self.ma2 = self.I(SMA, price, sma2)


    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()
    
def get_backtest(ticker, filename):
    if not ticker:
        ticker=input("Ticker Name: ")
    
    # ticker_df=get_history(symbol=ticker, start=date(2022,1,1), end=date(2023,4,9))
    ticker = yf.Ticker(ticker+".NS")
    data = ticker.history(period="1d",start="2022-01-01", end=None)


    bt = Backtest(data, SmaCross, commission=.002,
                exclusive_orders=True)
    stats = bt.run()
    bt.plot(filename=filename, open_browser=False)
