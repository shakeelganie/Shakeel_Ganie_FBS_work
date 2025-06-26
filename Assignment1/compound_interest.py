# calculate compound interest based on PTR

principle=int(input("Enter the principle amount: "))
time=int(input("Enter the number of years: "))
rate=float(input("Enter the rate of interest: "))
compound_interest=principle*(1+rate/100)**time-principle
print("The compound interest is: ",round(compound_interest,2))