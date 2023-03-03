from aiohttp import web
import sys
sys.path.insert(1, 'C:/Users/943602/Desktop/proj/sent/projo/Valuations')
import json
import valuation_determiner

routes = web.RouteTableDef()

@routes.get('/api/tickers')
async def tickers(request):
    with open("../Prerequisites/Tickers.csv") as f:
        cont = f.read().split()
        cont = cont[1:]
    
    return web.Response(text=json.dumps(cont))

@routes.get("/api/valuation/{ticker}")
async def valu(request):
    ticker = request.match_info["ticker"]
    t = valuation_determiner.valuation_determiner(ticker+".NS")
    
    return web.Response(text=json.dumps(t))    
    
app = web.Application()
app.add_routes(routes)
web.run_app(app)
