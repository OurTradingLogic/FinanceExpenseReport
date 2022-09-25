from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd 
import Mapping as map
import numpy as np

data = pd.read_excel('OpTransactionHistory29-05-2022.xls')
#print (data)

dataframe = pd.DataFrame()

Transac = 'Transaction Remarks'
Out = 'Withdrawal Amount (INR )'
In = 'Deposit Amount (INR )'
StartCol = 0
OutCol = 0
InCol = 0

for values in data.values:
    i = 0
    if StartCol == 0:
        for value in values:
            if Transac == value:
                StartCol = i
            if Out == value:
                OutCol = i
            if In == value:
                InCol = i
            i = i + 1
        continue  
    
    checkstr = str(values[StartCol])
    if checkstr == 'nan':
        continue
    
    dict = map.Search(values, StartCol, OutCol, InCol)
 
    if bool(dict):
        dataframe = dataframe.append(dict, ignore_index = True)
#
if dataframe.any:
    grp = dataframe.groupby(['Category'])
    df = grp.agg({'In' : 'sum', 'Out' : 'sum'})
    df.to_excel("output.xlsx")