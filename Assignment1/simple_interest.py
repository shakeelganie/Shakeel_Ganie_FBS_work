# Calculate the simple interest based on PTR

principle=int(input("Enter the principle amount: "))
time=int(input("Enter the number of years: "))
rate=float(input("Enter the rate of interest: "))

simple_interest=(principle*time*rate)/100

print("The simple interest is: ",simple_interest)