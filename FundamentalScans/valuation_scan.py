from valuation_f import *

#------------------------------------------------------------------------------------------
#returns a list of stocks that trades at a discount to its valuation as per book value

def sc_bookvalue():
    result=list()
    with open("FundamentalScans\\valuations_scans_result.csv",'r') as mf:
        data=csv.DictReader(mf)
        for row in data:
            if(float(row['LTP'])<float(row['VAP_BV'])):
                result.append(row['Ticker'])

    return result

#------------------------------------------------------------------------------------------
#returns a list of stocks that trades at a discount to its valuation as per sales

def sc_sales():
    result=list()
    with open("FundamentalScans\\valuations_scans_result.csv",'r') as mf:
        data=csv.DictReader(mf)
        for row in data:
            if(float(row['LTP'])<float(row['VAP_SALES'])):
                result.append(row['Ticker'])

    return result

#------------------------------------------------------------------------------------------
#returns a list of stocks that trades at a discount to its valuation as per graham number

def sc_graham():
    result=list()
    with open("FundamentalScans\\valuations_scans_result.csv",'r') as mf:
        data=csv.DictReader(mf)
        for row in data:
            if(float(row['LTP'])<float(row['VAP_GRAHAM'])):
                result.append(row['Ticker'])
                
    return result

#------------------------------------------------------------------------------------------
#returns a list of stocks that trades at a discount to its valuation as per earnings

def sc_earnings():
    result=list()
    with open("FundamentalScans\\valuations_scans_result.csv",'r') as mf:
        data=csv.DictReader(mf)
        for row in data:
            if(float(row['LTP'])<float(row['VAP_EARNINGS'])):
                result.append(row['Ticker'])

    return result
