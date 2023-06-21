import sys
from yahoofinancials import YahooFinancials
import sqlite3
import os
from flask import Flask, request, jsonify, Response,make_response
from flask.config import Config, ConfigAttribute
from flask_restful import Api, Resource
from flask_restful.utils import cors
from flask import send_file, send_from_directory#, safe_join, abort
from flask_cors import CORS, cross_origin
import sys


#sys.path.insert(1, os.path.join(os.getcwd(),'Sentiment\pcr'))
#import pcr_analyzer
from Sentiment import pcr_analyzer
from Valuations import valuation_determiner
from SWOT import swot_generator


app = Flask (__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)
api = Api(app)

api.decorators = [cors.crossdomain(origin='*', headers=['Content-Type', 'x-api-key', 'Authorization', 'Auth-Route', 'auto-key'])]

#TODO: reading .env file and incorporating library for managing variables
#TODO: incorporate posgres engine for relational and non-local databases
class Tickers(Resource):
    def get(self):
        
        directory = os.path.join(os.getcwd(),'Prerequisites/Tickers.csv')
        
        with open(directory) as f:
            cont = f.read().split()
            cont = cont[1:]
        return cont

api.add_resource(Tickers, '/api/tickers')


class Valuation(Resource):
    def get(self,ticker):
               
        t = valuation_determiner.valuation_determiner(ticker+".NS")
        t2 = valuation_determiner.financials_extractor(ticker+".NS")
        return jsonify({"v1":t, "v2": t2})

api.add_resource(Valuation, '/api/valuation/<ticker>')

class Valu(Resource):
    def get(self,ticker):
               
        t = valuation_determiner.valuation_determiner(ticker+".NS")
        t2 = valuation_determiner.financials_extractor(ticker+".NS")
        return jsonify({"v1":t, "v2": t2})

api.add_resource(Valu, '/api/sentiment/<ticker>')

class PcrAnal(Resource):
    def get(self,ticker):             
        
        if (ticker == "index"):
            data = pcr_analyzer.pcr_stocks_anal(ticker)
        else:
            data = pcr_analyzer.pcr_anal()
        return jsonify(data)

api.add_resource(PcrAnal, '/api/sentiment/pcrAnalyzer/<ticker>')


class Swot(Resource):
    def get(self,ticker):             
        
        data = swot_generator.swot_producer(ticker)
        return jsonify(data)

api.add_resource(Swot, '/api/swot/<ticker>')

class RegisterTrade(Resource):
    def post(self):             
        
        data = request.json()
        print(data)
        conn = sqlite3.connect('system.db')
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO TRADES VALUES ({data['id']}, '{data['tickerName']}', {data['type']}, '{data['enterPrice']}', '{data['exitPrice']}', {data['isOpen']})")
        conn.commit()
        conn.close()
        return jsonify({"success": "inserted"})

api.add_resource(RegisterTrade, '/api/registerTrade')

class Trade(Resource):
    def get(self,tradeID,exitPrice):             
        
        conn = sqlite3.connect('system.db')
        cursor = conn.cursor()
        cursor.execute(f"UPDATE TRADES SET exitPrice={exitPrice}, isOpen='0' WHERE id={tradeID}")
        conn.commit()
        conn.close()
        return jsonify({"success": "inserted"})

api.add_resource(Trade, '/api/swot/<tradeID>/<exitPrice>')

class Trades(Resource):
    def get(self,ticker):             
        
        conn = sqlite3.connect('system.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM TRADES WHERE tickerName='{ticker}'")
        output = cursor.fetchall()
        di = {"trades": []}
        for row in output:
            di["trades"].append(list(row))
        
        conn.commit()
        conn.close()
        return jsonify(di)

api.add_resource(Trades, '/api/trades/<ticker>')

class Ohlc(Resource):
    def get(self,ticker,interval):             
        
        yf = YahooFinancials(ticker+".NS")
        ohlc = yf.get_historical_price_data("2022-01-01","2023-03-11", interval)
        return jsonify(ohlc)

api.add_resource(Ohlc, '/api/ohlc/<ticker>/<interval>')


if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=5000, debug=False)