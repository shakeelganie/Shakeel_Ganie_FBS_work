# QNO: 8  Calculate to convert the days into years, weeks and days

days= int(input("Enter the number of days: "))
years=days//365
days=days%365
weeks=days//7
days=days%7
print("Total years are: ",round(years,2))
print("Total weeks are: ",round(weeks,2))
print("Total number of remaining days are: ",days)