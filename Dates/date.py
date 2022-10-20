import datetime

x = datetime.datetime.now()
print(x)
print(x.day)
print(x.month)
print(x.year)
print(x.strftime("%A"))


import datetime

x = datetime.datetime(2020, 5, 17)
print(x)

import datetime

x = datetime.datetime(2018, 3, 31)
print(x.strftime("%B"))

