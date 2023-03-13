import pandas_ta.momentum as ta


def indicators(df_sma, ma_length1, ma_length2, ma_length3):
    sma_1 = tuple(df_sma.ta.sma(ma_length1))
    sma_2 = tuple(df_sma.ta.sma(ma_length2))
    sma_3 = tuple(df_sma.ta.sma(ma_length3))
    rsi_tuple = tuple(ta.rsi(df_sma["close"][:-1]))
    
    return sma_1, sma_2, sma_3, rsi_tuple
