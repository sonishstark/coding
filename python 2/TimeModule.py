import datetime

#print(datetime.date.today())

now = datetime.datetime.today()

other = datetime.datetime(1994,10,10,17,59)
print(now-other)