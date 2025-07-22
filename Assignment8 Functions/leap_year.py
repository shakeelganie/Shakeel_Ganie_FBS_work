#  Write a program to check if entered year is a leap year or not.

def leapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap Year"
    else:
        return "It is not a leap year"
year=int(input("Enter the year: "))
result=leapYear(year)
print(result)
    