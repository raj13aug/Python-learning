#dt = datetime.datetime(2018, 1, 1)  --> (datetime.datetime) look ugly, so is better to import the data time class from this module.dont repeat datetime mutiple time.
#datetime.strptime --> converting string into a datatime object(Particularly useful when we get input from the user or read it from the file.)
#strftime --> convert a data time object into string

from datatime import datatime
import time

dt1 = datetime(2018, 1, 1)
dt2 = datatime.now()
dt = datatime.strptime("2018/01/01", "%Y/%m/%d")
dt = datatime.fromtimestamp(time.time())

print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))

print(dt2 > dt1)
