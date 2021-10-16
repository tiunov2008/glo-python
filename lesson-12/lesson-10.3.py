def days_in_month(month):
    monthes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return monthes[month - 1]
print(days_in_month(int(input())))