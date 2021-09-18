from datetime import datetime, timedelta, date, time
print((datetime.today()))
print((datetime.today())-timedelta(days=1))
print((datetime.today())-timedelta(days=30))
print(datetime.strptime('01/01/25 12:10','%d/%m/%Y %H:%m'))