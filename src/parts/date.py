### 62 ###
# date

import datetime

today = datetime.date.today() # date
now = datetime.datetime.now() # date + time
custom_date = datetime.datetime(2024, 11, 5, 10, 30, 45) # custom date

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def format_date(date):
    if date is None:
        month = months[now.month - 1]
        res = now.strftime(f"%H:%M:%S - %d {month} %Y")
    
        return res
    
    return custom_date.strftime(f"%H:%M:%S - %d {months[custom_date.month - 1]} %Y")

fd = format_date(None)
cfd = format_date(custom_date)

print(f"Today:\n{fd}")
print()

if now < custom_date:
    print(f"# The date \"{cfd}\" has not passed.")
else:
    print(f"# The date \"{cfd}\" has passed.")