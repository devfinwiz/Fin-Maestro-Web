import os
import pandas


def consolidating(df, percentage=2):
    recent_candlesticks = df[-5:]

    max_close = recent_candlesticks['Close'].max()
    min_close = recent_candlesticks['Close'].min()

    threshold = 1 - (percentage / 100)
    if min_close > (max_close * threshold):
        return True

    return False


def breaking_out(df, percentage=2.5):
    last_close = df[-1:]['Close'].values[0]

    if consolidating(df[:-1], percentage=percentage):
        recent_closes = df[-6:-1]

        if last_close > recent_closes['Close'].max():
            return True

    return False


for filename in os.listdir('C:/Users/osk/Desktop/TY Project/candlestick-pattern-analyzer/data/stocks/'):
    df = pandas.read_csv(
        'C:/Users/osk/Desktop/TY Project/candlestick-pattern-analyzer/data/stocks/{}'.format(filename))

    if consolidating(df, percentage=2.5):
        print("{} is consolidating".format(filename))

    if breaking_out(df):
        print("{} is breaking out".format(filename))
