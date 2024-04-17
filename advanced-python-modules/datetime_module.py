
import datetime
from datetime import date

sample_time = datetime.time(3, 20)
print(sample_time)
print(sample_time.hour)
print(sample_time.minute)

print(datetime.date.today())
print(datetime.date.today().year)

created_dt = datetime.datetime(2024, 4, 25, 11, 30, 45)
print(created_dt)

created_dt = created_dt.replace(month=1)
print(created_dt)

date_1 = date(2024, 4, 25)
date_2 = date(2023, 4, 25)

date_diff = date_1 - date_2
print(date_diff)
print(type(date_diff))
print(date_diff.days)

# ----- @TODO Console Output -----

# 03:20:00
# 3
# 20
# 2024-04-17
# 2024
# 2024-04-25 11:30:45
# 2024-01-25 11:30:45
# 366 days, 0:00:00
# <class 'datetime.timedelta'>
# 366
#
# Process finished with exit code 0




