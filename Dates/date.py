
import datetime

## Date Output
#x = datetime.datetime.now()
#print(x)

x = datetime.datetime.now()
print(x)
print(x.strftime("%A"))

## Date Objects

x = datetime.datetime(2022, 12, 31)
print(x)

x = datetime.datetime(2018, 6, 1)
#print(x.strftime('%B'))
#print(x.strftime('%a'))
#print(x.strftime('%p'))

import datetime

time = datetime.datetime.now()

print(time)
print(time.strftime('%p'))
