import sys
from questdb.ingress import Sender, IngressError
import psycopg as pg
sys.path.append("init")
sys.path.append("Valuations")
from init import *
import pandas as pd
import heapq

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Returns a dictionary with key financials of requested ticker
#Demo result= {'bookValue': 237.74, 'priceToBook': 2.03, 'trailingEPS': 14.84, 'priceToSales': 7.31, 'priceToEarnings': 32.53, 'close': 482.75}

def financials_extractor(ticker):       #with QuestDb cache support

    discard=[]
    result={}
    
    conn_str = 'user=admin password=quest host=127.0.0.1 port=8812 dbname=qdb'
    with pg.connect(conn_str, autocommit=True) as connection:
        with connection.cursor() as cur:

            #Query the database and obtain data as Python objects.

            cur.execute('SELECT * FROM stock_financials;')
            records = cur.fetchall()

            for row in records:
                if row[0]==ticker:
                    result['ticker']=row[0]
                    result['bookValue']=row[1]
                    result['priceToBook']=row[2]
                    result['trailingEPS']=row[3]
                    result['promoterHolding']=row[4]
                    result['priceToSales']=row[5]
                    result['priceToEarnings']=row[6]
                    result['close']=row[7]
                    return result
                
    try:
        yf=YahooFinancials(ticker)
        d_stats=yf.get_key_statistics_data()
        d_sum=yf.get_summary_data()
        
        result['ticker']=ticker
        result['bookValue']=round(d_stats[ticker]['bookValue'],2)
        result['priceToBook']=round(d_stats[ticker]['priceToBook'],2)
        result['trailingEPS']=d_stats[ticker]['trailingEps']
        result['promoterHolding']=round(d_stats[ticker]['heldPercentInsiders']*100,2)

        result['priceToSales']=round(d_sum[ticker]['priceToSalesTrailing12Months'],2)
        result['priceToEarnings']=round(d_sum[ticker]['previousClose']/d_stats[ticker]['trailingEps'],2)
        result['close']=d_sum[ticker]['previousClose']

        df2=pd.DataFrame([result])
    
        try:
            host: str = 'localhost' 
            port: int = 9009
            with Sender(host, port) as sender:
                sender.dataframe(
                    df2,
                    table_name='stock_financials',  # Table name to insert into.
                    symbols=['ticker'],  # Columns to be inserted as SYMBOL types.
                    )  # Column containing the designated timestamps.

        except IngressError as e:
            sys.stderr.write(f'Got error: {e}\n')
    
    except Exception as e:
        discard.append(ticker)
        print(e)

    return result

def valuation_determiner(ticker):
    data=financials_extractor(ticker) 
    
    mono_duo=['BSE.NS','IEX.NS','CDSL.NS','MCX.NS']
    fmcg=['TATACONSUM.NS','ITC.NS','VBL.NS','UBL.NS','MARICO.NS','DABUR.NS','BRITANNIA.NS','COLPAL.NS','MCDOWELL-N.NS','NESTLEIND.NS','PGHH.NS','HIDUNILVR.NS','GODREJCP.NS','EMAMILTD.NS','RADICO.NS']
    bank=['KOTAKBANK.NS','HDFCBANK.NS','ICICIBANK.NS','AXISBANK.NS','SBIN.NS']
    it=['TCS.NS','INFY.NS','TECHM.NS']

    #-------------------------------------------------------------------------------
    #VAP (Valuation As Per) Book Value

    max_threshhold=1.8 #Max desired priceToBook
    val_bv=0 #Valuation as per book value
    pricetobook=float(data['priceToBook'])
    ltp=float(data['close'])
    valuation_result={}
    valuation_result['TICKER']=ticker

    if(ticker in mono_duo or ticker in fmcg or ticker in bank):
        max_threshhold=2.4
        percent_appreciation=((max_threshhold-pricetobook)/pricetobook)*100
        val_bv=ltp+((ltp*percent_appreciation)/100)
    elif(pricetobook<1.8):
        percent_appreciation=((max_threshhold-pricetobook)/pricetobook)*100
        val_bv=ltp+((ltp*percent_appreciation)/100)
    elif(pricetobook>1.8):
        percent_depreciation=((pricetobook-max_threshhold)/pricetobook)*100
        val_bv=ltp-((ltp*percent_depreciation)/100)
    else:
        val_bv=ltp 
    valuation_result['VAP_BV']=round(val_bv,2)

    #-------------------------------------------------------------------------------
    #VAP (Valuation As Per) Sales

    max_threshhold=1.5 #Max desired priceToSales
    val_sales=0 #valuation as per sales
    pricetosales=float(data['priceToSales'])

    if(ticker in mono_duo or ticker in fmcg or ticker in bank):
        max_threshhold=2.0
        percent_appreciation=((max_threshhold-pricetosales)/pricetosales)*100
        val_sales=ltp+((ltp*percent_appreciation)/100)
    elif(pricetosales<1.5):
        percent_appreciation=((max_threshhold-pricetosales)/pricetosales)*100
        val_sales=ltp+((ltp*percent_appreciation)/100)
    elif(pricetosales>1.5):
        percent_depreciation=((pricetosales-max_threshhold)/pricetosales)*100
        val_sales=ltp-((ltp*percent_depreciation)/100)
    else:
        val_sales=ltp 
    valuation_result['VAP_SALES']=round(val_sales,2)

    #-------------------------------------------------------------------------------
    #VAP (Valuation As Per) Graham Number

    trailing_EPS=float(data['trailingEPS'])
    book_value=float(data['bookValue'])

    try:
        val_graham=math.sqrt(22.5*trailing_EPS*book_value)
        valuation_result['VAP_GRAHAM']=round(val_graham,2)
    except:
        valuation_result['VAP_GRAHAM']="NA"

    #-------------------------------------------------------------------------------
    #VAP (Valuation As Per) Earnings

    if(ticker in mono_duo or ticker in fmcg or ticker in bank):
        #print("here3")
        valuation_result['VAP_EARNINGS']=round(27*trailing_EPS,2)
        if(valuation_result['VAP_EARNINGS']<0):
            valuation_result['VAP_EARNINGS']=0.00
    else:
        valuation_result['VAP_EARNINGS']=round(16*trailing_EPS,2)
        if(valuation_result['VAP_EARNINGS']<0):
            valuation_result['VAP_EARNINGS']=0.00

    valuation_result['LTP']=ltp

    #---------------------------------------------------------------------------------------------------------------------------------------------
    #Status: Overvalued/ Fairly valued/ Undervalued

    valuation_average=(valuation_result['VAP_BV']+valuation_result['VAP_SALES']+valuation_result['VAP_GRAHAM']+valuation_result['VAP_EARNINGS'])/4
    if(ticker in mono_duo or ticker in bank or ticker in fmcg or ticker in it):
        valuation_result['TICKER']=0
        lar1=max(list(valuation_result.values()))
        lar2=heapq.nlargest(2, valuation_result.values())[1]
        valuation_average=(lar1+lar2)/2
        valuation_average=valuation_average+(18*valuation_average/100)
        valuation_result['TICKER']=ticker
    
    hold=abs(valuation_result['LTP']-valuation_average)/min(valuation_result['LTP'],valuation_average)*100

    if(hold<=3.1):
        valuation_result['STATUS']="Fairly Valued"
    elif(valuation_result['LTP']<valuation_average):
        valuation_result['STATUS']="Undervalued"
    else:
        valuation_result['STATUS']="Overvalued"

    valuation_result['FAIR_VALUE']=round(valuation_average,2)
    #val_list = [str(i) for i in valuation_result.values()]
    
    '''with open("FundamentalScans\\valuations_scans_result.csv",'a') as f:
        line = ','.join(val_list)
        line+="\n"
        f.write(line)'''

    df2=pd.DataFrame([valuation_result])
    
    try:
            host: str = 'localhost' 
            port: int = 9009
            with Sender(host, port) as sender:
                sender.dataframe(
                    df2,
                    table_name='stock_valuations',  # Table name to insert into.
                    symbols=['TICKER'],  # Columns to be inserted as SYMBOL types.
                    )  # Column containing the designated timestamps.

    except IngressError as e:
            sys.stderr.write(f'Got error: {e}\n')
    
def get_symbols():
    flag=1
    comp=csv.reader(open(r"Prerequisites\Tickers.csv"))     
    tickers=[]
    
    for c in comp:
        if(flag==1):
            flag=0
            continue
        
        symbol=c[0]
        tickers.append(symbol+".NS")
        
    return tickers

if __name__=='__main__':
     tickers=get_symbols()
     with concurrent.futures.ThreadPoolExecutor() as executor:
         executor.map(valuation_determiner,tickers)

