#!/usr/bin/env python3
'''
https://python-scripts.com/datetime-time-python
https://pythonworld.ru/moduli/modul-datetime.html
https://docs.python.org/3/library/datetime.html
'''
from datetime import datetime
from time import sleep
def convert_string_to_time(date_string):
    from datetime import datetime
    date_time_obj = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S.%f')
    return date_time_obj

#date_string = '2019-02-11 20:16:04.157254'    
date_string = str(datetime.now())
print (date_string)
print (str(datetime.now()).split(' '))
date_time = convert_string_to_time(date_string)
print (date_time)
sleep(0.050000)
print (datetime.now())
delta=datetime.now()- date_time
print (delta)
print(delta.days)
print(delta.seconds)
print(delta.microseconds)
if  delta.microseconds > 200000 : print ("> 200000")
elif delta.microseconds < 100000 : print ("< 100000")
else : print (delta.microseconds)
print (delta.microseconds)