#1
from datetime import date, timedelta 

day = date.today() - timedelta(5)
print("Current date is ", date.today())
print("Before 5 days ", day)

#2
from datetime import date, timedelta
tod = date.today()
yes = date.today() - timedelta(1)
tom = date.today() + timedelta(1)
print("Yesterday :",yes)
print("Today :", tod )
print("Tomorrow :", tom)

#3
import datetime
a = datetime.datetime.now()
b = datetime.datetime.now().replace(microsecond=0)
print(a)
print(b)

#4
from datetime import date, datetime,timedelta,time
a = datetime.today()
b = datetime.strptime("10 October 2023, 17:23:45", "%d %B %Y, %H:%M:%S")
c = (a-b).seconds
print(datetime.today())
print(c)
