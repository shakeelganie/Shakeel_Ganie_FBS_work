# calculate the total salary of an employee based on basic, DA= 10% of basic, TA= 12% of basic, HRA= 15% of basic

basic_salary=int(input("Enter the basic salary of an employee: "))
da=10*basic_salary/100
ta=12*basic_salary/100
hra=15*basic_salary/100
total_salary=basic_salary+da+ta+hra
print("Total salary of an employee is: ",total_salary)