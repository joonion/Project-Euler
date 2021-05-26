def is_leapyear(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    return False

def days(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 29 if is_leapyear(year) else 28

def solve(year_from, year_to, weekday):
    count = 0
    for year in range(year_from, year_to + 1):
        for month in range(1, 13):
            weekday = (weekday + days(year, month)) % 7
            count += 1 if weekday == 0 else 0
    return count

year_from, year_to = 1901, 2000
# If we assume that Sunday is 0, 
# the day of week at 1 Jan 1901 is Tuesday(2),
# Monday(1) + 365 // 7 = 2. 
answer = solve(year_from, year_to, 2)
print(answer)

