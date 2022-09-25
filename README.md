# FinanceExpenseReport

This report will help to categories our transactions with specific grouping like 'Expense', 'Investment', 'Retriement', 'Bills', 'Loans', 'Returns', 'EmergencyFund'... Also, uncategorised transaction with group separately and it will come to our notice for further check. 

e.g., If bank charged any amount under SUR-CHARGES, GST like that then it will export in output file with full transaction description in seperate row and come to our notice.

Prerequisite:
1. Basic Python Code Setup- refer https://youtu.be/iQPbnTteGs4
2. Install yfinance package- refer https://youtu.be/zyiKntx7r6c
3. Bollinger Band Indicator- refer https://youtu.be/OpAVgTVLs0I
4. Use Git, Google Colab and Googlt Drive- refer https://youtu.be/wG_D32kq9zo

## Make below changes for setup with your own bank statement:

>In Main.py
```
data = pd.read_excel('OpTransactionHistory29-05-2022.xls') 
``` 
- Replace 'OpTransactionHistory29-05-2022' in above code with your exported bank statement excel file name.
```
Transac = 'Transaction Remarks'
Out = 'Withdrawal Amount (INR )'
In = 'Deposit Amount (INR )'
```
- Replace 'Transaction Remarks' string in above code with transaction description column name on your statement file.
- Replace 'Withdrawal Amount (INR )' string in above code with money out column name on your statement file.
- Replace 'Deposit Amount (INR )' string in above code with money in column name on your statement file.

>In Mapping.py
```
def Search(values, StartCol, OutCol, InCol):
```
- Based on transaction description, the above method will categories the transaction.
```
if outStr in Expense:
    outStr = 'Expense'
elif outStr in Investment:
    outStr = 'Investment'
elif outStr in Retriement:
    outStr = 'Retriement'
elif outStr in Bills:
    outStr = 'Bills'
elif outStr in Loans:
    outStr = 'Loans'
elif outStr in Returns:
    outStr = 'Returns'
elif outStr in EmergencyFund:
    outStr = 'EmergencyFund'
```
- More grouping happing under 'Expense', 'Investment', 'Retriement', 'Bills', 'Loans', 'Returns', 'EmergencyFund' on above code
```
dict = { 'Category': outStr, 'In': In, 'Out': Out }
```
- This is a output column grouping

## Find Output in output.xlsx

### Please customise your own category in Mapping.py file based on your transaction statement and requirement.

