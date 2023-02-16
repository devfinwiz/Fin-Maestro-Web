from yahoofinancials import YahooFinancials
import math

#------------------------------------------------------------------------------------------------
#Returns a dictionary with key financials of requested ticker
#Demo result= {'bookValue': 442.3, 'priceToBook': 0.86, 'trailingEPS': 45.83, 'promoterHolding': 55.54, 'priceToSales': 0.41, 'close': 376.45}

def financials_extractor(ticker):
    discard=[]
    result=dict()

    try:
        yf=YahooFinancials(ticker)
        d_stats=yf.get_key_statistics_data()
        print("here")
        d_sum=yf.get_summary_data()

        result['bookValue']=round(d_stats[ticker]['bookValue'],2)
        result['priceToBook']=round(d_stats[ticker]['priceToBook'],2)
        result['trailingEPS']=d_stats[ticker]['trailingEps']
        result['promoterHolding']=round(d_stats[ticker]['heldPercentInsiders']*100,2)

        result['priceToSales']=round(d_sum[ticker]['priceToSalesTrailing12Months'],2)
        result['close']=d_sum[ticker]['previousClose']
    
    except Exception as e:
        discard.append(ticker)
        print(e)

    return result

#---------------------------------------------------------------------------------------------------------
#Returns a dictionary containing valuations as per different parameters for a ticker
#Demo result= {'TICKER': 'ADSL.NS', 'VAP_BV': 190.39, 'VAP_SALES': 183.21, 'VAP_GRAHAM': 158.94, 'VAP_EARNINGS': 174.24}

def valuation_determiner(ticker):
    data=financials_extractor(ticker) 
    mono_duo=['BSE.NS','IEX.NS','CDSL.NS','MCX.NS']
    #-------------------------------------------------------------------------------
    #VAP (Valuation As Per) Book Value

    max_threshhold=1.8 #Max desired priceToBook
    val_bv=0 #Valuation as per book value
    pricetobook=data['priceToBook']
    ltp=data['close']
    valuation_result=dict()
    valuation_result['TICKER']=ticker

    if(ticker in mono_duo):
        max_threshhold=2.1
        percent_appreciation=((max_threshhold-pricetobook)/pricetobook)*100
        val_bv=ltp+((ltp*percent_appreciation)/100)
    elif(data['priceToBook']<1.8):
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
    pricetosales=data['priceToSales']

    if(ticker in mono_duo):
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

    trailing_EPS=data['trailingEPS']
    book_value=data['bookValue']
    
    val_graham=math.sqrt(22.5*trailing_EPS*book_value)
    valuation_result['VAP_GRAHAM']=round(val_graham,2)

    #-------------------------------------------------------------------------------
    #VAP (Valuation As Per) Earnings
    if(ticker in mono_duo):
        #print("here3")
        valuation_result['VAP_EARNINGS']=round(27*trailing_EPS,2)
    else:
        valuation_result['VAP_EARNINGS']=round(16*trailing_EPS,2)

    return valuation_result

#---------------------------------------------------------------------------------------------------------------
#Method call
#print(valuation_determiner("MCX.NS"))
