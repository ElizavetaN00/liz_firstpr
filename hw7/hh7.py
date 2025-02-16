# 1 Time
n = int(input("Enter the number that displays on motorbike: "))
number_of_hours = n//60
# number_of_minutes = n - (number_of_hours*60)
number_of_minutes = n % 60
if number_of_hours < 10:
    if number_of_minutes < 10:
        print(f"0{number_of_hours}:0{number_of_minutes}")
    else:
        print(f"0{number_of_hours}:{number_of_minutes}")
else:
    print(f"{number_of_hours}:{number_of_minutes}")

sum_of_digits = ((number_of_hours//10) + (number_of_hours % 10)
                 + (number_of_minutes//10) + (number_of_minutes % 10))
print("Summ of digits:", sum_of_digits)

# 2 Level Up
experience = int(input("Enter XP: "))
threshold = int(input("Enter next level's threshold: "))
reward = int(input("Enter the points for killing the monster: "))

if experience + reward >= threshold:
    result = True
else:
    result = False

print(result)

# 3 Time converter
time_24 = '23:15'
hours, minutes = time_24.split(':')
hours = int(hours)
minutes = int(minutes)

if hours < 12:
    period = 'a.m.'
    if hours == 0:
        hours = 12
elif hours > 12:
    period = 'p.m.'
    hours -= 12
else:
    period = 'p.m.'
    hours == 12

if minutes < 10:
    minutes_str = '0' + str(minutes)
else:
    minutes_str = str(minutes)

if hours < 10:
    time_12 = str(hours) + ':' + minutes_str + ' ' + period
else:
    time_12 = str(hours) + ':' + minutes_str + ' ' + period

print(time_12)

