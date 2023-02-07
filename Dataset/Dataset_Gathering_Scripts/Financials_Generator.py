from yahoofinancials import YahooFinancials
import csv
import concurrent.futures
from itertools import zip_longest

symbol=0
remover,tickers_list=[],[]

#-------------------------------------------------------------------------------------------------------------------------
#Returns various key financial metrics for a ticker

def financials_fetcher(ticker):
        try:
            yahoo_financials=YahooFinancials(ticker)
            hold=yahoo_financials.get_key_statistics_data()
            hold2=yahoo_financials.get_summary_data()
            hold3=yahoo_financials.get_financial_stmts('annual', 'income')
            book_value=hold[ticker]['bookValue']
            EVtoEBITDA=hold[ticker]['enterpriseToEbitda']
            priceToBookR=hold[ticker]['priceToBook']
            market_cap=(hold2[ticker]['marketCap'])//10000000
            priceToSales=(hold2[ticker]['priceToSalesTrailing12Months'])
            previous_Close=(hold2[ticker]['previousClose'])
            sharesOutstanding=hold[ticker]['sharesOutstanding']
            total_revenue=hold3["incomeStatementHistory"][ticker][0]['2022-03-31']['totalRevenue']

        except:
            remover.append(ticker)
            print(remover)
        
        try:
            return ticker,book_value,EVtoEBITDA,priceToBookR,market_cap,priceToSales,previous_Close,sharesOutstanding,total_revenue
        except:
            return ticker,None,None,None,None,None,None,None,None

#------------------------------------------------------------------------------------------------------------------------------------
#Executes financial_fetcher() for all tickers in Tickers.csv using threads and stores output in Financials.csv

def thread_pool_executor():

    comp=csv.reader(open("Prerequisites\Tickers.csv"))

    for c in comp:
        tickers_list.extend(c)

    with concurrent.futures.ThreadPoolExecutor() as executor:
    
        tickers=tickers_list[1:]
        results=executor.map(financials_fetcher,tickers)

        ticker_results,tickers_book_value,tickers_evtoebitda,tickers_priceToBook,tickers_close=[],[],[],[],[]
        tickers_marketcap,tickers_priceToSales,tickers_sharesoutstanding,tickers_total_revenue=[],[],[],[]

        for result in results:
                
                    ticker_results.append(result[0])
                    tickers_book_value.append(result[1])
                    tickers_evtoebitda.append(result[2])
                    tickers_priceToBook.append(result[3])
                    tickers_marketcap.append(result[4])
                    tickers_priceToSales.append(result[5])
                    tickers_close.append(result[6])
                    tickers_sharesoutstanding.append(result[7])
                    tickers_total_revenue.append(result[8])


    list_clubber=[ticker_results,tickers_book_value,tickers_evtoebitda,tickers_priceToBook,tickers_marketcap,tickers_priceToSales,tickers_close,tickers_sharesoutstanding,tickers_total_revenue]
    export_data=zip_longest(*list_clubber,fillvalue='')

    with open("Financials.csv",'a',encoding="ISO-8859-1",newline='') as myfile:
        wr=csv.writer(myfile)
        #wr.writerow(("Ticker","Book Value"))
        wr.writerows(export_data)
    myfile.close()

    holder=list()

    with open("Financials.csv",'r') as f:
        csvreader=csv.reader(f)
        for row in csvreader:
            holder.append(row)
            if not row[1]:
                holder.remove(row)

    with open("Financials.csv",'w',newline='') as fw:
        writer=csv.writer(fw)
        writer.writerows(holder) 
    print("Success")

#----------------------------------------------------------------------------------------------
#Method call

thread_pool_executor()

