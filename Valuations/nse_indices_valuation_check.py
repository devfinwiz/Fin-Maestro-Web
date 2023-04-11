import pandas as pd

NSE_INDICES = ["NIFTY 50",
               "NIFTY NEXT 50",
               "NIFTY 100",
               "NIFTY 200",
               "NIFTY 500",
               "NIFTY MIDCAP 50",
               "NIFTY MIDCAP 100",
               "NIFTY SMALLCAP 100",
               "NIFTY AUTO",
               "NIFTY BANK",
               "NIFTY ENERGY",
               "NIFTY FMCG",
               "NIFTY IT",
               "NIFTY MEDIA",
               "NIFTY METAL",
               "NIFTY PHARMA",
               "NIFTY PSU BANK",
               "NIFTY REALTY",
               "NIFTY COMMODITIES",
               "NIFTY CPSE",
               "NIFTY MNC",
               "NIFTY PSE",
               "NIFTY SHARIAH 25",
               "NIFTY50 SHARIAH",
               "NIFTY500 SHARIAH",
               "NIFTY100 EQUAL WEIGHT",
               "NIFTY ALPHA 50",
               "NIFTY HIGH BETA 50",
               "NIFTY LOW VOLATILITY 50",
               "NIFTY50 VALUE 20"             
               ]

#-----------------------------------------------------------------------------------------------------------------------------
#Returns a dictionary with flag color alloted for each indice indicating their health depending upon their present valuation
#Demo Output: 
#{'NIFTY 50': 'GREEN', 'NIFTY NEXT 50': 'ORANGE', 'NIFTY 100': 'GREEN', 'NIFTY 200': 'GREEN', 'NIFTY 500': 'GREEN', 'NIFTY MIDCAP 50': 'GREEN', 'NIFTY MIDCAP 100': 'GREEN', 'NIFTY SMALLCAP 100': 'GREEN', 'NIFTY AUTO': 'GREEN', 
#'NIFTY BANK': 'GREEN', 'NIFTY ENERGY': 'ORANGE', 'NIFTY FMCG': 'GREEN', 'NIFTY IT': 'GREEN', 'NIFTY MEDIA': 'GREEN', 'NIFTY METAL': 'RED', 'NIFTY PHARMA': 'GREEN', 'NIFTY PSU BANK': 'GREEN', 'NIFTY REALTY': 'GREEN', 
#'NIFTY COMMODITIES': 'RED', 'NIFTY CPSE': 'GREEN', 'NIFTY MNC': 'GREEN', 'NIFTY PSE': 'RED', 'NIFTY SHARIAH 25': 'GREEN', 'NIFTY50 SHARIAH': 'GREEN', 'NIFTY500 SHARIAH': 'GREEN', 'NIFTY100 EQUAL WEIGHT': 'ORANGE', 
#'NIFTY ALPHA 50': 'GREEN', 'NIFTY HIGH BETA 50': 'ORANGE', 'NIFTY LOW VOLATILITY 50': 'GREEN', 'NIFTY50 VALUE 20': 'ORANGE'}

def indices_flag_allocator():
    indices_flag=dict()
    indices_median_pe=dict()
    indices_latest_pe=dict()
    exceptions=['NIFTY FMCG','NIFTY IT']

    for indice in NSE_INDICES:
        df=pd.read_csv("..\\Dataset\Resultant Dataset\\nse_indices_pe_dataset\\{}.csv".format(indice))
        indices_median_pe[indice]=round(df['P/E'].median(),2)
        indices_latest_pe[indice]=df['P/E'].iloc[-1]
    
    for indice,value in indices_median_pe.items():
        if(indice in exceptions and (value + (75*value)/100)<indices_latest_pe[indice]):
            indices_flag[indice]="RED"
        elif(indice in exceptions and (value + (20*value)/100)<indices_latest_pe[indice]):
            indices_flag[indice]="ORANGE"
        elif(indice in exceptions and (value + (20*value)/100)>indices_latest_pe[indice]):
            indices_flag[indice]="GREEN"

        if((value + (30*value)/100)<indices_latest_pe[indice] and indice not in exceptions):
            indices_flag[indice]="RED"
        elif((value + (6*value)/100)<indices_latest_pe[indice] and indice not in exceptions):
            indices_flag[indice]="ORANGE"
        else:
            if(indice not in exceptions):
                indices_flag[indice]="GREEN"

    #print(indices_median_pe)
    return indices_flag

#--------------------------------------------------------------------------------------------------------
#Method call

# print(indices_flag_allocator())

#--------------------------------------------------------------------------------------------------------
#Returns a dictionary with median PE of each NSE indice
'''def indices_median_pe():
    median_pe=dict()
    for indice in NSE_INDICES:
        df=pd.read_csv("Dataset\\Resultant Dataset\\nse_indices_pe_dataset\\{}.csv".format(indice))
        median_pe[indice]=round(df['P/E'].median(),2)
    return median_pe'''
