import csv

def first_col(file_relative_path): 
    hold=[]
    with open("{}".format(file_relative_path)) as f:
        for row in f:
            hold.append(row.split(',')[0])
    hold2=[[i[1:-1]] for i in hold]
    return hold2


def store_in_tickers_csv():
    hold=first_col("Prerequisites\NSE_BSE_CSV_Bunch\MW-NIFTY-SMALLCAP-250-05-Feb-2023.csv")
    with open('Prerequisites\Tickers.csv','w',newline="") as f:
        writer = csv.writer(f)
        writer.writerows(hold)
        
store_in_tickers_csv()
   