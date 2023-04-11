import sys
from yahoofinancials import YahooFinancials
import sqlite3
from aiohttp import web
import requests
import time

sys.path.insert(1, 'C:/Users/943602/Desktop/proj/sent/projo/Valuations')
sys.path.insert(1, 'C:/Users/943602/Desktop/proj/sent/projo/Backtest')
sys.path.insert(1, 'C:/Users/943602/Desktop/proj/sent/projo/FundamentalScans')
sys.path.insert(1, 'C:/Users/943602/Desktop/proj/sent/projo')
sys.path.insert(1, 'C:/Users/943602/Desktop/proj/sent/projo/Sentiment')
sys.path.insert(1, 'C:/Users/943602/Desktop/proj/sent/projo/Sentiment/pcr')
sys.path.insert(1, 'C:/Users/943602/Desktop/proj/sent/projo/SWOT')
import json
import pcr_analyzer
import valuation_determiner
import nse_indices_valuation_check
import swot_generator
import valuation_scan
import sma_crossover
# from news import fetchnews, analy
import logging

logging.basicConfig(level=logging.DEBUG)

routes = web.RouteTableDef()

@routes.get('/api/tickers')
async def tickers(request):
    with open("../Prerequisites/Tickers.csv") as f:
        cont = f.read().split()
        cont = cont[1:]
    
    return web.Response(text=json.dumps(cont))

@routes.get('/api/filterTickers/{filter}')
async def tickers(request):
    filter = request.match_info["filter"]
    if (" " in filter):
        return web.Response(text=json.dumps({"tickers":[]}))
        
    headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'accept-encoding' : 'gzip, deflate, br',
        'accept-language' : 'en-US,en;q=0.9'
    }
    url = f"https://query2.finance.yahoo.com/v1/finance/search?q={filter}&lang=en-US&region=US&quotesCount=6&newsCount=2&listsCount=2&enableFuzzyQuery=false&quotesQueryId=tss_match_phrase_query&multiQuoteQueryId=multi_quote_single_token_query&newsQueryId=news_cie_vespa&enableCb=true&enableNavLinks=true&enableEnhancedTrivialQuery=true&enableResearchReports=true&enableCulturalAssets=true&enableLogoUrl=true&researchReportsCount=2"
    req = requests.get(url, headers=headers)
    data = json.loads(req.content.decode('utf-8'))
    tickers = []
    if (data["count"] > 0):
        for i in data["quotes"]:
            if i.get("exchange") == "NSI":
                tickers.append([i["symbol"].split(".")[0], i["longname"], i["shortname"]])
                
    return web.Response(text=json.dumps({"tickers":tickers}))

@routes.get("/api/valuation/{ticker}")
async def valu(request):
    ticker = request.match_info["ticker"]
    if (ticker != "index"):
        t = valuation_determiner.valuation_determiner(ticker+".NS")
        t2 = valuation_determiner.financials_extractor(ticker+".NS")
    
        return web.Response(text=json.dumps({"v1":t, "v2": t2}))
    else:
        d = nse_indices_valuation_check.indices_flag_allocator()
        return web.Response(text=json.dumps(d))


@routes.get("/api/sentiment/{ticker}")
async def valu(request):
    ticker = request.match_info["ticker"]
    t = valuation_determiner.valuation_determiner(ticker+".NS")
    t2 = valuation_determiner.financials_extractor(ticker+".NS")
    
    return web.Response(text=json.dumps({"v1":t, "v2": t2}))    

@routes.get("/api/ohlc/{ticker}/{interval}")
async def valu(request):
    ticker = request.match_info["ticker"]
    interval = request.match_info["interval"]
    yf = YahooFinancials(ticker+".NS")
    ohlc = yf.get_historical_price_data("2022-01-01","2023-03-28", interval)
    return web.Response(text=json.dumps(ohlc))

@routes.get("/api/sentiment/pcrAnalyzer/{ticker}")
async def pcrAnal(request):
    ticker = request.match_info["ticker"]
    if (ticker != "index"):
        data = pcr_analyzer.pcr_stocks_anal(ticker)
    else:
        data = pcr_analyzer.pcr_anal()
    return web.Response(text=json.dumps(data))


@routes.get("/api/swot/{ticker}")
async def swot(request):
    ticker = request.match_info["ticker"]
    data = swot_generator.swot_producer(ticker+".NS")
    return web.Response(text=json.dumps(data))

@routes.post("/api/registerTrade")
async def registerTrade(request):
    data = await request.json()
    conn = sqlite3.connect('system.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO TRADES(`ID`, `tickerName`, `type`, `enterPrice`, `exitPrice`, `isOpen`) VALUES ({data['id']}, '{data['tickerName']}', {data['type']}, '{data['enterPrice']}', '{data['exitPrice']}', {data['isOpen']})")
    conn.commit()
    conn.close()
    return web.Response(text=json.dumps({"success": "inserted"}))

@routes.get("/api/closeTrade/{tradeID}/{tickerName}/{exitPrice}")
async def valu(request):
    conn = sqlite3.connect('system.db')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE TRADES SET exitPrice={request.match_info['exitPrice']}, isOpen='0' WHERE id={request.match_info['tradeID']} and tickerName='{request.match_info['tickerName']}'")
    conn.commit()
    conn.close()
    return web.Response(text=json.dumps({"success": "inserted"}))

@routes.get("/api/trades/{ticker}")
async def valu(request):
    conn = sqlite3.connect('system.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM TRADES WHERE tickerName='{request.match_info['ticker']}'")
    output = cursor.fetchall()
    di = {"trades": []}
    for row in output:
        di["trades"].append(list(row))

    conn.commit()
    conn.close()
    return web.Response(text=json.dumps(di))
    
@routes.get("/api/fundamental")
async def valu(request):
    data = {
        "bookValue": valuation_scan.sc_bookvalue(),
        "sales": valuation_scan.sc_sales(),
        "graham": valuation_scan.sc_graham(),
        "earnings": valuation_scan.sc_earnings(),
    }
    
    return web.Response(text=json.dumps(data))

@routes.get("/api/genBacketst/{ticker}")
async def genBacktest(request):
    ticker = request.match_info["ticker"]
    ts = time.time()
    sma_crossover.get_backtest(ticker,f"C:/Users/943602/Desktop/proj/sent/projo/server/static/charts/{ts}.html")
    return web.Response(text=json.dumps({"fname":str(ts)+".html"}))

app = web.Application()
app.add_routes(routes)
app.add_routes([web.static('/static', "static")])
web.run_app(app, port=8081)
