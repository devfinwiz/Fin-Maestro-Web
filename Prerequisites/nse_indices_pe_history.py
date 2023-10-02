import sys
sys.path.append("init")
from init import *
import datetime
from constants import NSE_INDICES

#---------------------------------------------------------------------------
#Generates csv files for all NSE indices with their PE,P/B

def dataset_generator(indice):  
    history_filename=r"Dataset\Resultant Dataset\\nse_indices_pe_dataset\{}.csv".format(indice)  
    f=open(history_filename,'w',newline="")

    symbol="{}".format(indice)
    start_date = "01-Jan-2021"
    end_date = "02-Oct-2023"

    indice_pe = index_pe_pb_div(symbol,start_date,end_date)
    #print(indice_pe)
    f.write(indice_pe.to_csv())
    f.close()

if __name__=='__main__':
     with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(dataset_generator,NSE_INDICES)
