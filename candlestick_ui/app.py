import os
import csv
import talib
import pandas
import array as arr
import yfinance as yf
import json
from flask import Flask, request, render_template
from patterns import candlestick_patterns
from datetime import date

app = Flask(__name__)


@app.route('/getjson')
def getjson():
    ticker = request.args.get('symbol', None)
    if ticker is None:
        return {
            "error": "No symbol found."
        }
    else:
        ticker = ticker.upper()
        path = os.path.join(os.getcwd(), "data", "stocks", ticker+".csv")
        return csv_to_json(path)


@app.route('/scanner')
def scanner():
    pattern = request.args.get('pattern', False)
    fet = request.args.get('fet')
    stock_list = request.args.get('state', state())
    stocks = {}

    with open('data/symbols.csv') as f:
        for row in csv.reader(f):
            stocks[row[0]] = {'company': row[1]}

    if pattern:
        for filename in os.listdir('data/stocks'):
            df = pandas.read_csv('data/stocks/{}'.format(filename))
            pattern_function = getattr(talib, pattern)
            symbol = filename.split('.')[0]

            try:
                results = pattern_function(
                    df['Open'], df['High'], df['Low'], df['Close'])
                results.iloc[::-1]

                last = results.tail(50).values[0]
                i = 0
                for j in reversed(results):
                    if last == 0:
                        last = int(j)
                    if last != 0:
                        break

                    if i == 50:
                        break

                    i += 1

                if last > 0:
                    stocks[symbol][pattern] = 'BULLISH'
                    stocks[symbol]["day"] = i
                    print(i)
                elif last < 0:
                    stocks[symbol][pattern] = 'BEARISH'
                    stocks[symbol]["day"] = i
                    print(i)
                else:
                    stocks[symbol][pattern] = None
            except Exception as e:
                print('Failed on File: ', filename, e)
    if fet:
        fetch_data()

    return render_template('scanner.html',
                           candlestick_patterns=candlestick_patterns,
                           stocks=stocks, pattern=pattern, fet=fet,
                           state=stock_list, active='scanner')


@app.route('/about')
def about():
    return render_template('about.html', active="about")


@app.route('/patterns')
def patterns():
    return render_template('patterns.html', active="pattern")


@app.route('/fetch_data')
def fetch_data():
    current_date = str(date.today())
    with open('data/symbols.csv') as f:
        for line in f:
            if "," not in line:
                continue
            symbol = line.split(",")[0]
            # print(symbol)
            data = yf.download(
                # date format: yyyy-mm-dd
                symbol + '.NS', start="2020-01-01", end="{}".format(current_date))
            data.to_csv('data/stocks/{}.csv'.format(symbol))

    return {
        "code": "success"
    }


@app.route('/')
def index():
    return render_template('index.html', active='home')


@app.route('/state')
def state():
    consolidate_stock = arr.array('b', [])  # a1
    consolidate_stock = "Consolidating:\n"
    breakout_stock = arr.array('b', [])  # a2
    breakout_stock = "Breaking Out:\n"

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

    for filename in os.listdir('data/stocks/'):
        df = pandas.read_csv('data/stocks/{}'.format(filename))

        if consolidating(df, percentage=2.5):
            a1 = "{}".format(filename.strip('.csv')) + "\n"
            consolidate_stock += a1

        if breaking_out(df):
            a2 = "{}".format(filename.strip('.csv')) + "\n"
            breakout_stock += a2

        stock_list = consolidate_stock + "\n" + breakout_stock

    return stock_list


def csv_to_json(csvFilePath):
    jsonArray = []

    # read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
    jsonString = json.dumps(jsonArray, indent=4)
    return jsonString
