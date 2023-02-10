import csv 

#-------------------------------------------------------------------------------------------------------
#Returns valuation of the requested ticker as per its book value

def valuation_book_value(ticker):
    with open("Dataset\Resultant Dataset\Financials.csv",'r') as f:
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
    with open("Dataset\Resultant Dataset\Financials.csv",'r') as f:
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

print(valuation_book_value("GRAPHITE.NS"))
print(valuation_sales("GRAPHITE.NS"))