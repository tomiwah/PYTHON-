#profit=[]
#take_home = []

def t_bills(amount, days, rate):
    profit = (days/365) * (rate/100) * amount
    take_home = (amount) + (profit)
    print (profit)
    print(' you will be paid {} Naira'.format(take_home))
    #return profit, take_home


    

