import csv 
import math

#-------------------------------------------------------------------------------------------------------
#Returns valuation of the requested ticker as per its book value

def valuation_book_value(ticker):
    with open(r"Dataset\Resultant Dataset\Financials.csv",'r') as f:
        reader=csv.DictReader(f)
        for row in reader:
            if(row['Ticker']==ticker):
                pricetobook=float(row['PricetoBook'])
                ltp=float(row['Close'])
                break
            
        max_threshhold=1.8 #Max desired priceToBook
        val_bv=0 #valuation as per book value
        
        if(pricetobook<1.8):
            percent_appreciation=((max_threshhold-pricetobook)/pricetobook)*100
            val_bv=ltp+((ltp*percent_appreciation)/100)
        elif(pricetobook>1.8):
            percent_depreciation=((pricetobook-max_threshhold)/pricetobook)*100
            val_bv=ltp-((ltp*percent_depreciation)/100)
        else:
            val_bv=ltp 
        f.close()
        
    return round(val_bv,2)

#-------------------------------------------------------------------------------------------------------
#Returns valuation of the requested ticker as per its annual sales

def valuation_sales(ticker):
    with open(r"Dataset\Resultant Dataset\Financials.csv",'r') as f:
        reader=csv.DictReader(f)
        for row in reader:
            if(row['Ticker']==ticker):
                pricetosales=float(row['PricetoSales'])
                ltp=float(row['Close'])
                break 
        
        max_threshhold=1.5 #Max desired priceToSales
        val_sales=0 #valuation as per sales
        
        if(pricetosales<1.5):
            percent_appreciation=((max_threshhold-pricetosales)/pricetosales)*100
            val_sales=ltp+((ltp*percent_appreciation)/100)
        elif(pricetosales>1.5):
            percent_depreciation=((pricetosales-max_threshhold)/pricetosales)*100
            val_sales=ltp-((ltp*percent_depreciation)/100)
        else:
            val_sales=ltp 
        f.close()

    return round(val_sales,2)

#-------------------------------------------------------------------------------------------------------
#Returns valuation of the requested ticker as per Graham

def valuation_graham(ticker):
    with open(r"Dataset\Resultant Dataset\Financials.csv",'r') as f:
        reader=csv.DictReader(f)
        for row in reader:
            if(row['Ticker']==ticker):
                trailingeps=float(row['TrailingEPS'])
                pricetobook=float(row['PricetoBook'])
                ltp=float(row['Close'])
                break 
                
        if(pricetobook>1):
            percentdiff=((pricetobook-1)/pricetobook)*100
            book_value=ltp-(ltp*percentdiff)/100
        elif(pricetobook<1):
            percentdiff=(1-pricetobook)/1*100
            book_value=ltp+(ltp*percentdiff)/100
        else:
            book_value=ltp 
        
        val_graham=math.sqrt(22.5*trailingeps*book_value)
        f.close()
    
    return round(val_graham,2)     

#-------------------------------------------------------------------------------------------------------
#Returns valuation of the requested ticker as per its earnings

def valuation_earnings(ticker):
    with open(r"Dataset\Resultant Dataset\Financials.csv",'r') as f:
        reader=csv.DictReader(f)
        for row in reader:
            if(row['Ticker']==ticker):
                trailingeps=float(row['TrailingEPS'])
                break 
    
    return round(12.5*trailingeps,2)

#method call 
print(valuation_earnings("GRAPHITE.NS"))
