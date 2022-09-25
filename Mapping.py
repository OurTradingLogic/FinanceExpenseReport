

from numpy import nan

Expense = ['Hi' , 'hello', 'at', 'this', 'there', 'from']
Investment = ['Mutual Fund' , 'Gold Online', 'Stock', 'Zerodha', 'there', 'from']
Retriement = ['Post Office' , 'Life Insurance Bill', 'this', 'there', 'from']
Bills = ['Credit Card Bill' , 'Rent Amount', 'EB Bill', 'Mobile', 'there', 'from']
Loans = ['For Loan Payment', 'hello', 'at', 'this', 'there', 'from']
Returns = ['Stock Dividend']
EmergencyFund = ['**Customise String for grouping***']

#While doing online transfer, use specific comment and use it here for maintain finance
def OnlineTranfer(stri):
    if '***Mention comment which you used for online transfer***' in stri:
        outStr = '***Customise String***'
    elif '***Mention comment which you used for online transfer***' in stri:
        if '***Mention comment which you used for online transfer***' in stri:
            outStr = '**Customise String***'
        else: outStr = '**Customise String***'
    else: 
        outStr = 'Transfer Online'
    return outStr

def BillPayment(stri):
    if 'CREDIT' in stri:
        outStr = 'Credit Card Bill'
    elif '/LIFE INSUR' in stri:
        outStr = 'Life Insurance Bill'
    elif '/EB' in stri:
        outStr = 'EB Bill'
    elif 'SBI MUTUAL' in stri or 'NIPPON IND' in stri or 'MOTILAL OS' in stri:
        outStr = 'Mutual Fund'
    elif 'ONE97 COMM' in stri:
        outStr = 'Mobile'
    elif 'IMPS' in stri or 'NEFT' in stri:
        outStr = OnlineTranfer(stri)
    else:
        outStr = 'Bill'
    return outStr

def UPI(stri):
    if 'PAYMENT' in stri:
        outStr = 'UPI Payment'
    elif '@' in stri:
        outStr = 'Transfer from UPI address'
    else:
        outStr = 'Transfer UPI' 
    return outStr

def Search(values, StartCol, OutCol, InCol):
    In = values[InCol]
    Out = values[OutCol]

    if str(In) == 'nan' and str(Out) == 'nan':
        return {}

    stri1 = values[StartCol]
    outStr = str(stri1)
    stri = outStr.upper()
    if 'ACH' in stri:
        if 'SAFEGOLD' in stri:
            outStr = 'Gold Online'
        else:
            outStr = 'Stock Dividend'
    elif 'FDR-BOND' in stri:
        outStr = 'Gold Bond'
    elif 'MF-' in stri:
        outStr = 'Mutual Fund' 
    elif 'BHARTI AIRTEL' in stri or 'AIRTEL DIRECT' in stri:
        outStr = 'Mobile'
    elif '***Give your Loan Number***' in stri:
        outStr = 'For Loan Payment'
    elif '***Mention if you get salery from specific client***' in stri:
        outStr = 'Salery'
    elif 'EBA/NSE' in stri or 'EBA/BSE' in stri:
        outStr = 'Stock'
    elif 'INT.PD' in stri:
        outStr = 'Interest Rate'
    elif 'CHG/' in stri and 'ATM' in stri:
        outStr = 'ATM Charges'
    elif 'CHG/' in stri and 'POS' in stri:
        outStr = 'Pos Charge'
    elif 'DP CHGS TILL' in stri:
        outStr = 'DP Charge TILL'
    elif 'SURCHARGE' in stri:
        outStr = 'Surcharge'
    elif 'ZERODHA' in stri:
        outStr = 'Zerodha'
    elif 'RAILWAY' in stri:
        outStr = 'RailWay'
    elif 'LPCHE' in stri:
        outStr = 'Loan'
    elif 'AMZN' in stri:
        outStr = 'Amazon'
    elif '/ZOMATO MED' in stri:
        outStr = 'Zomato'
    elif 'UPI' in stri:
        outStr = UPI(stri)           
    elif '/GPAY/' in stri:
        outStr = 'Google Pay'
    elif '/CASH WDL/' in stri:
        outStr = 'Cash'
    elif 'BIL/' in stri:
        outStr = BillPayment(stri)    
    elif 'INFT' in stri:
        outStr = 'Internal Fund Transfer'
    elif 'APY' in stri:
        outStr = 'Pension'
    elif 'BAJAJ_AUTO_CD' in stri:
        outStr = 'EMI'
    elif 'NETFLIX' in stri:
        outStr = 'Netflix'
    elif 'VPS' in stri or 'IPS' in stri:
        outStr = 'Debit Card Transaction'
    elif 'IMPS' in stri or 'NEFT' in stri:
        outStr = OnlineTranfer(stri)

    #Grouping under 'Expense', 'Investment', 'Retriement', 'Bills', 'Loans', 'Returns', 'EmergencyFund'
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

    dict = { 'Category': outStr, 'In': In, 'Out': Out }
    return dict

    