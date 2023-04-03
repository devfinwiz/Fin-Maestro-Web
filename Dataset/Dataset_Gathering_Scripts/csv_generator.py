from nsepy import get_history
import csv 
from datetime import date
from dateutil.relativedelta import relativedelta
import concurrent.futures

def get_symbols():
    flag=1
    comp=csv.reader(open(r"Prerequisites\Tickers.csv"))     
    tickers=[]
    
    for c in comp:
        if(flag==1):
            flag=0
            continue
        
        symbol=c[0]
        tickers.append(symbol)
        
    return tickers
        
def dataset_generator(symbol):
    
    current_date = date.today()
    start_date = current_date - relativedelta(years=1)
    failure=[]

    #Creation of individual CSVs for all listed tickers in Tickers.csv

    history_filename=r"Dataset\Resultant Dataset\\ticker_csvs\{}.csv".format(symbol)  
    f=open(history_filename,'w',newline="")

    #---------------------------------------------------------------------------------
    #Data being fetched from nsepy and then being written in individual Ticker's CSV
    
    try:
        df=get_history(symbol=symbol,start=start_date,end=current_date)
        f.write(df.to_csv())
        f.close()
    except:
        failure.append(symbol)
        
if __name__=='__main__':
     tickers=get_symbols()
     with concurrent.futures.ThreadPoolExecutor() as executor:
         executor.map(dataset_generator,tickers)
        