from Valuations.valuation_determiner import financials_extractor,valuation_determiner

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Returns a dictionary with swot analysis for requested ticker
#Demo result: 
# {'Strength': {'Attractive P/B Ratio': 'ADSL.NS is available at priceToBook of 0.96'}, 'Weakness': {}, 'Opportunity': {'Attractive P/S and P/B': 'ADSL.NS is available with priceToSales of 0.84 and priceToBook of 0.96', 
# 'Attractive Valuations': "ADSL.NS last traded price is trading at 74.15'%' discount to its valuation as per earnings.", 'Undervalued': 'ADSL.NS is trading below the graham number by 58.86%'}, 'Threat': {}}

def swot_producer(ticker):
    data=financials_extractor(ticker)
    valuation=valuation_determiner(ticker)
    swot=dict()
    s,w,o,t=dict(),dict(),dict(),dict()

    mono_duo=['BSE.NS','IEX.NS','CDSL.NS','MCX.NS']
    fmcg=['TATACONSUM.NS','ITC.NS','VBL.NS','UBL.NS','MARICO.NS','DABUR,NS','BRITANNIA.NS','COLPAL.NS','MCDOWELL-N.NS','NESTLEIND.NS','PGHH.NS','HIDUNILVR.NS','GODREJCP.NS','EMAMILTD.NS','RADICO.NS']
    bank=['KOTAKBANK.NS','HDFCBANK.NS','ICICIBANK','AXISBANK','SBIN.NS']

    promoterHolding=data['promoterHolding']
    priceToSales=data['priceToSales']
    priceToBook=data['priceToBook']
    pe=data['priceToEarnings']

    if(ticker not in mono_duo and ticker not in fmcg and ticker not in bank):
        if(promoterHolding>69.99):
            s['HighPromoterHolding']=ticker+" has promoter holding of "+str(promoterHolding)+"%"
        if(priceToBook<1.5):
            s['Attractive P/B Ratio']=ticker+" is available at priceToBook of "+str(priceToBook)
        
        if(priceToSales>1.8):
            w['Unattractive P/S Ratio']=ticker+ " is available at priceToSales of "+str(priceToSales)
        if(priceToBook>1.9):
            w['Unattractive P/B Ratio']=ticker+" is available at priceToBook of "+str(priceToBook)
        
        if(priceToBook<1.0 and priceToSales<1):
            o['Attractive P/S and P/B']=ticker+ " is available with priceToSales of "+str(priceToSales)+" and priceToBook of "+str(priceToBook)
        if(valuation['VAP_EARNINGS']>valuation['LTP']):
            percent=round((valuation['VAP_EARNINGS']-valuation['LTP'])/valuation['LTP']*100,2)
            o['Attractive Valuations']=ticker+ ' last traded price is trading at '+str(percent)+"'%' discount to its valuation as per earnings."
        if(valuation['VAP_GRAHAM']>valuation['LTP']):
            percent=round((valuation['VAP_GRAHAM']-valuation['LTP'])/valuation['LTP']*100,2)
            o['Undervalued']=ticker+" is trading below the graham number by "+str(percent)+"%"

        if(promoterHolding<40):
            t['Low Promoter Holding']=ticker+" has low promoter holding of "+str(promoterHolding)+"%"
        if(pe>40):
            t['High PE']=ticker+" has a PE of "+str(pe)

    else:
        if(promoterHolding>69.99):
            s['HighPromoterHolding']=ticker+" has promoter holding of "+str(promoterHolding)+"%"
        if(priceToBook<1.8):
            s['Attractive P/B Ratio']=ticker+" is available at priceToBook of "+str(priceToBook)
        
        if(priceToBook>3.6):
            w['Unattractive P/B Ratio']=ticker+" is available at priceToBook of "+str(priceToBook)

        if(priceToBook<1.5 and priceToSales<1.5):
            o['Attractive P/S and P/B']=ticker+ " is available with priceToSales of "+str(priceToSales)+" and priceToBook of "+str(priceToBook)
        if(valuation['VAP_EARNINGS']>valuation['LTP']):
            percent=round((valuation['VAP_EARNINGS']-valuation['LTP'])/valuation['LTP']*100,2)
            o['Attractive Valuations']=ticker+ ' last traded price is trading at a discount of '+str(percent)+"'%' in comparsion to its valuation as per earnings."
        if(valuation['VAP_GRAHAM']>valuation['LTP']):
            percent=round((valuation['VAP_GRAHAM']-valuation['LTP'])/valuation['LTP']*100,2)
            o['Undervalued']=ticker+" is trading below the graham number by "+str(percent)+"%"

        if(pe>40):
            t['High PE']=ticker+" has a PE of "+str(pe)

    swot['Strength'],swot['Weakness'],swot['Opportunity'],swot['Threat']=s,w,o,t 
    return swot

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Method call

#print(swot_producer("ADSL.NS"))

