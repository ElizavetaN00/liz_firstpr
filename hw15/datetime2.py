from datetime import datetime


def check_date_status(date_str):
    now = datetime.today()
    date_conversion = datetime.strptime(date_str, "%Y-%m-%d")

    if date_conversion > now:
        return "Entered date is a future date"
    elif date_conversion < now:
        return "Entered date is a date from the past"
    else:
        return "Entered date is current"


date3 = input('Enter any date in format "YYYY-MM-DD": ')
result = check_date_status(date3)
print(result)
