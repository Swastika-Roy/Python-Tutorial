import calendar

def print_cal(y):
    for m in range(1, 13):  # Loop through all 12 months
        print(calendar.month(y, m))  # Print each month

print_cal(2017)