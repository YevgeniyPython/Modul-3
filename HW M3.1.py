from datetime import datetime

def get_days_from_today(date):
    try:
        mydate = datetime.strptime(date, "%Y-%m-%d")
        datenow = datetime.today()
        difference = datenow.toordinal() - mydate.toordinal()
        return difference
    except ValueError:
        return f"time data {date} does not match format '%Y-%m-%d'"
    


print(get_days_from_today("2024-4-12"))
print(get_days_from_today("202-12"))