import csv 
from itertools import filterfalse        

#----------------------------------------------------------------------------------
#Identify and remove duplicates from Tickers.csv

def unique_everseen(iterable, key=None):
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in filterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element        

with open("Prerequisites\Tickers.csv", "r") as file:
    lines = []
    for line in file:
        lines.append(line.strip("\n").split(","))

with open("Prerequisites\Tickers.csv", "w") as file:
    for line in unique_everseen(lines, key=frozenset):
        file.write(",".join(line)+"\n")
        
#------------------------------------------------------------------------------------
#Example of how to append exchange extention .NS or .BO as needed. 

'''def append_exchange_suffix():
    tickers_pre_extension=[]
    tickers_post_extension=[]
    flag=0
    
    with open("Prerequisites\Tickers.csv",'r') as f:
        pass 
        reader=csv.DictReader(f)
        for rows in reader:
            tickers_pre_extension.append(rows['Ticker'])
    
    for ticker in tickers_pre_extension:
        if(ticker=='DIVISLAB')
        tickers_post_extension.append(str(ticker)+str(".NS"))
    
    return tickers_post_extension

print(append_exchange_suffix())'''