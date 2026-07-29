def add(a,b):
    return a+b


def sub(a,b):
    return a - b



import math

print(dir(math))
help(math.sqrt)


import math 
print(math.sqrt(25))
print(math.ceil(25.5))
print(math.floor(25.5))
print(math.pi)

import os
print(os.getcwdb)
print(os.listdir)
print(os.mkdir('new folder'))


import sys
print(sys.path)


from datetime import datetime,date,timedelta
now = datetime.now()
print(now.year, now.month, now.day)
print(now.strftime('%H: %M: %S'))
today= date.today()
print(today)
tomorrow = today + timedelta(days = 1)
print(tomorrow)
diff = datetime(2025,1,1) - datetime.now()
print(diff)