import csv
import re
import pandas as pd

#------------------------------------------------------------------------------------------------------
#List of raw csv files from where symbols are to be extracted.

files=[
    'Prerequisites\\NSE_BSE_CSV_Bunch\\MW-NIFTY-SMALLCAP-100-05-Feb-2023.csv','Prerequisites\\NSE_BSE_CSV_Bunch\\MW-NIFTY-SMALLCAP-250-05-Feb-2023.csv','Prerequisites\\NSE_BSE_CSV_Bunch\\MW-NIFTY-SMALLCAP-50-05-Feb-2023.csv',
    'Prerequisites\\NSE_BSE_CSV_Bunch\\MW-NIFTY-NEXT-50-05-Feb-2023.csv','Prerequisites\\NSE_BSE_CSV_Bunch\\MW-NIFTY-MIDSMALLCAP-400-05-Feb-2023.csv','Prerequisites\\NSE_BSE_CSV_Bunch\\MW-NIFTY-MIDCAP-150-05-Feb-2023.csv',
    'Prerequisites\\NSE_BSE_CSV_Bunch\\MW-NIFTY-MIDCAP-100-05-Feb-2023.csv','Prerequisites\\NSE_BSE_CSV_Bunch\\MW-NIFTY-MIDCAP-50-05-Feb-2023.csv','Prerequisites\\NSE_BSE_CSV_Bunch\\MW-NIFTY-200-05-Feb-2023.csv',
    'Prerequisites\\NSE_BSE_CSV_Bunch\\MW-NIFTY-100-05-Feb-2023.csv','Prerequisites\\NSE_BSE_CSV_Bunch\\MW-NIFTY-50-05-Feb-2023.csv'
    ]

#------------------------------------------------------------------------------------------------------
#Returns a list of symbols from a passed csv file as arguement

def first_col(file_relative_path): 
    hold=[]
    with open("{}".format(file_relative_path)) as f:
        for row in f:
            hold.append(row.split(',')[0])
    hold2=[[i[1:-1]] for i in hold]
    return hold2

#------------------------------------------------------------------------------------------------------
#Stores the symbols in Tickers.csv after correcting symbols with inappropriate characters

def store_in_tickers_csv():
    for file in files:
        hold=first_col("{}".format(file))
        
        for i in range(len(hold)):
            if('"' in str(hold[i])):
                #print("here")
                correct_ticker = re.sub(r'[^a-zA-Z\d\s]', u'', str(hold[i]), flags=re.UNICODE)
                hold[i]=str(correct_ticker).split(",")

        with open(r'Prerequisites\Tickers.csv','a',newline="") as f:
            writer = csv.writer(f)
            writer.writerows(hold)
    

store_in_tickers_csv()