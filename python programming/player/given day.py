import datetime as dt

day = dt.datetime.strptime('2012-02-03','%Y-%m-%d').date()
print day#day=2012-03-02 (Friday)

if day.weekday()==4:
    day = day+dt.timedelta(days=3)
else:
    day = day+dt.timedelta(days=1)

print day#day=2012-02-06 (Monday)
day = day+dt.timedelta(days=1)
print day#day=2012-02-07 (Tuesday)
