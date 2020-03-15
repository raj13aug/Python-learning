from datatime import datatime, timedelta

dt1 = datatime(2018, 1, 1) + timedelta(days=1, seconds=1)
print(dt1)
dt2 = datatime.now()

duration = dt2 - dt1
print(duration)
print("days", duration.days)
print("seconds", duration.seconds)
print("total_seconds", duration.total_seconds())

# data time objects, these objects represent a point in time. In datatime module also class called time delta, which represents a duration.

# why youre wondering why we don't have month or year here, the reason is that we can have a varying amount of time in a montha or in year,That's why only days, seconds and microseconds.
