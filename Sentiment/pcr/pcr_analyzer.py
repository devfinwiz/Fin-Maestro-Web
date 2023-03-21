from pcr_scraper import pcr_scraper,pcr_stocks_scraper

#-----------------------------------------------------------------------------------------------------------------------------------------
#Returns a dictionary indicating state of indice (overbought/slightly overbought,oversold,slightly oversold) along with present pcr_value
#Demo Output: {'NIFTY': ['Slightly overbought', 1.269], 'BANKNIFTY': ['Slightly overbought', 1.343]}

def pcr_anal():
    pcr_anal_result=dict()
    indices=["NIFTY","BANKNIFTY"]

    for symbol in indices:
        try:
            pcr_value=pcr_scraper(symbol)
        except:
            try: 
                pcr_value=pcr_scraper(symbol)
            except:
                try:
                    pcr_value=pcr_scraper(symbol)
                except:
                    pcr_value=pcr_scraper(symbol)

        if(pcr_value>=1.4):
            state="Overbought"
            pcr_anal_result[symbol]=[state,pcr_value]
        elif(pcr_value<1.4 and pcr_value>=1):
            state="Slightly overbought"
            pcr_anal_result[symbol]=[state,pcr_value]
        elif(pcr_value<1 and pcr_value>=0.6):
            state="Slightly oversold"
            pcr_anal_result[symbol]=[state,pcr_value]
        else:
            state="Oversold"
            pcr_anal_result[symbol]=[state,pcr_value]
        
    return pcr_anal_result

#-----------------------------------------------------------------------------------------------------------------------------------------
#Returns a dictionary indicating state of stock (overbought/slightly overbought,neutral,oversold,slightly oversold) along with present pcr_value
#Demo Output: {'ADANIENT': ['Neutral', 0.662]}

def pcr_stocks_anal(symbol):
    try:
        pcr_anal_result=dict()
        pcr_value=pcr_stocks_scraper(symbol)
    except:
        try:
            pcr_value=pcr_stocks_scraper(symbol)
        except:
            try:
                pcr_value=pcr_stocks_scraper(symbol)
            except:
                pcr_value=pcr_stocks_scraper(symbol)

    if(pcr_value>=1):
        state="Overbought"
        pcr_anal_result[symbol]=[state,pcr_value]
    elif(pcr_value<1 and pcr_value>=0.75):
        state="Slightly overbought"
        pcr_anal_result[symbol]=[state,pcr_value]
    elif(pcr_value<0.75 and pcr_value>=0.50):
        state="Neutral"
        pcr_anal_result[symbol]=[state,pcr_value]
    elif(pcr_value<0.50 and pcr_value>=0.4):
        state="Slightly oversold"
        pcr_anal_result[symbol]=[state,pcr_value]
    else:
        state="Oversold"
        pcr_anal_result[symbol]=[state,pcr_value]
        
    return pcr_anal_result


#--------------------------------------------------------------
#method call

print(pcr_stocks_anal("ADANIENT"))
