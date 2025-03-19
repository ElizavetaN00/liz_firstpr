from dateutil.parser import parse


def date_difference_in_days(date1, date2):
    dt1 = parse(date1)
    dt2 = parse(date2)
    difference_in_days = (dt2 - dt1).days
    return abs(difference_in_days)


date1 = input('Enter first date in format "YYYY-MM-DD": ')
date2 = input('Enter second date in format "YYYY-MM-DD": ')

difference = date_difference_in_days(date1, date2)
print(f"Difference between {date1} and {date2} is "
      f"{difference} day(s)")
