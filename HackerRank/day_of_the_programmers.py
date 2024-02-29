"""
Given a year "y", find the date of the 256th day of that year according to the official Russian calendar during that year. Then print it in the format dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit month, and yyyy is "y" (year).

From 1700 to 1917, Russia's official calendar was the Julian calendar; since 1919 they used the Gregorian calendar system. The transition from the Julian to Gregorian calendar system occurred in 1918, when the next day after January 31st was February 14th. This means that in 1918, February 14th was the 32nd day of the year in Russia.

In both calendar systems, February is the only month with a variable amount of days; it has 29 days during a leap year, and 28 days during all other years. 

In the Julian calendar: 
    - Divisible by 4 

In the Gregorian calendar:
    - Divisible by 400.
    - Divisible by 4 and not divisible by 100.

========SAMPLE========

Input:
y = 2016

Output:
12.09.2016

EXPLANATION:

The year 2016 is a leap year, so February has 29 days but all the other months have the same number of days as in 2017. When we sum the total number of days in the first eight months, we get 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 = 244. Day of the Programmer is the 256th day, so then calculate 256 - 244 = 12 to determine that it falls on day 12 of the 9th month (September). We then print the full date in the specified format, which is 12.09.2016.
"""

month_name2number = {"January": 1,
                     "February": 2,
                     "March": 3,
                     "April": 4,
                     "May": 5,
                     "June": 6,
                     "July": 7,
                     "August": 8,
                     "September": 9,
                     "October": 10,
                     "November": 11,
                     "December": 12}


selected_day = 256

def day_programmers(year: int):
    calendar = {"January": 31,
                "February": 28,
                "March": 31,
                "April": 30,
                "May": 31,
                "June": 30,
                "July": 31,
                "August": 31,
                "September": 30,
                "October": 31,
                "November": 30,
                "December": 31}
    
    if year > 1918:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            calendar["February"] += 1
    elif year < 1918:
        if year % 4 == 0:
            calendar["February"] += 1
    elif year == 1918:
        calendar["February"] -= 13

    day = 0
    month = ""
    for next_month in calendar.keys():
        if day > selected_day:
            break
        day += calendar[next_month]
        month = next_month
        
    diference = day - selected_day
        
    actual_day = str(calendar[month] - diference)
    if len(actual_day) < 2:
        actual_day = f"0{actual_day}"

    actual_month = str(month_name2number[month])
    if len(actual_month) < 2:
        actual_month = f"0{actual_month}"

    actual_year = str(year)

    return f"{actual_day}.{actual_month}.{actual_year}"
    

print(day_programmers(1918))
print(day_programmers(2017))
print(day_programmers(2016))
print(day_programmers(1800))
