# Counting Sundays
# Problem 19

# You are given the following information, but you may prefer to do some research for yourself.
#   1 Jan 1900 was a Monday.
#   Thirty days has September,
#   April, June and November.
#   All the rest have thirty-one,
#   Saving February alone,
#   Which has twenty-eight, rain or shine.
#   And on leap years, twenty-nine.
#   A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# Answer: 171


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


def days_of_month(year, month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 30


def main():
    sundays = 0
    year, month, week = 1901, 0, 2
    while year <= 2000:
        week = (week + days_of_month(year, month+1)) % 7
        if week == 0:
            sundays += 1
        month = (month + 1) % 12
        if month == 0:
            year = year + 1
    print(sundays)


if __name__ == '__main__':
    main()
