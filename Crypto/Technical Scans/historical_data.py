import sys
import time
import pandas as pd
from binance.client import Client
import frameselect


class BinanceTicker:
    def __init__(self, ticker_binance, time_frame_binance):
        self.ticker = ticker_binance
        self.time_frame = time_frame_binance
        self.client = Client("", "", tld="com")
        self.file_name = self.ticker + ".csv"
        self.header_list = [
            "unix",
            "open",
            "high",
            "low",
            "close",
            "volume",
            "close time",
            "Volume USDT",
            "tradecount",
            "taker buy vol",
            "taker buy quote vol",
            "ignore",
        ]

    def check_pair(self, ticker_symbol):
        """
        Checks if the given ticker symbol is a valid pair.
        :param ticker_symbol: The ticker symbol to check.
        :return: True if the ticker symbol is a valid pair, False otherwise.
        """
        if self.client.get_symbol_info(ticker_symbol):
            print("Pair found in Binance API.")
            return self.client.get_symbol_info(ticker_symbol)
        else:
            print("Pair is not found in Binance API.")
            sys.exit()

    def historical_data_write(self):
        """
        Writes the historical data for a given ticker symbol to a csv file.
        """
        df = pd.DataFrame(
            reversed(
                user_ticker.client.get_historical_klines(
                    symbol=self.ticker, interval=self.time_frame, start_str=start
                )
            ),
            columns=self.header_list,
        )
        # Converting the unix time to a readable date format for today
        date = pd.to_datetime(df["unix"], unit="ms")
        df.insert(1, "date", date)
        df.drop(
            labels=[
                "volume",
                "close time",
                "tradecount",
                "taker buy vol",
                "taker buy quote vol",
                "ignore",
            ],
            inplace=True,
            axis=1,
        )
        with open(self.file_name, "w") as f:
            df.to_csv(f, index=False)

if len(sys.argv) == 3:
    ticker, frame_s = sys.argv[1].upper(), sys.argv[2].upper()
else:
    # Example input:"BTCUSDT 1H", "ETHBTC 3D", "BNBUSDT 15M"
    print("Ticker and Time Frame: ")
    ticker, frame_s = str(input().upper()).split()
binance_api_runtime = time.perf_counter()
time_frame, start = frameselect.frame_select(frame_s)
user_ticker = BinanceTicker(ticker, time_frame)
user_ticker.check_pair(ticker)

