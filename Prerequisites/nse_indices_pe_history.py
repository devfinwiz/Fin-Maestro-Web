import datetime
from constants import NSE_INDICES
from nsepy import get_index_pe_history
import concurrent.futures

#---------------------------------------------------------------------------
#Generates csv files for all NSE indices with their PE,P/B

def dataset_generator(indice):  
    history_filename=r"Dataset\Resultant Dataset\\nse_indices_pe_dataset\{}.csv".format(indice)  
    f=open(history_filename,'w',newline="")

    indice_pe = get_index_pe_history(symbol="{}".format(indice),
                                    start=datetime.datetime(2022,1,1),
                                    end=datetime.datetime(2023,2,17))
    f.write(indice_pe.to_csv())
    f.close()

if __name__=='__main__':
     with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(dataset_generator,NSE_INDICES)
