import datetime as dt
print(dt.datetime.now())
print(dt.datetime.now().year)
print(dt.datetime.now()-dt.datetime(2025,8,31))
print(dt.datetime.strftime(dt.datetime.now(),"%B %d, %Y")) #%Y: year, %B: month, %d: day