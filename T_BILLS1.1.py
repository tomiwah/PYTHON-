rate = 12.5
from datetime import datetime
from datetime import timedelta
from datetime import date



print("Hello Investor, how much would you like to invest in the treasury bills?")
amount=int(input())
print("how many days wll you like your investment to run for?")
no_days = int(input())
date = date.today() + timedelta(days=no_days)
d = (no_days/365)
r = (rate/100)
interest = d * r * amount
print(interest)
Total = amount + interest
print("the current interest rate today is " + str(rate) + "%")
print("your investment will mature on the " + str(date.strftime('%d %b, %Y')))
print("your interest will be " + str(interest))
print("Total amount paid into your account will be " + str(Total))

