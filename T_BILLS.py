profit=[]
def t_bills(amount, days,rate):
    profit = (days/365) * (rate/100) * amount
    return profit
print (profit)
