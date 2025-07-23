# calculate the basic salary of n employees

def calculate_total_salaries(n):
    
    total_all_employees = 0

    for i in range(1, n+1):
        basic = float(input(f"Enter basic salary of employee {i}: "))

        if basic < 2000:
            da = 0.10 * basic
            ta = 0.12 * basic
            hra = 0.15 * basic
        else:
            da = 0.15 * basic
            ta = 0.18 * basic
            hra = 0.20 * basic

        total_salary = basic + da + ta + hra
        print(f"Total salary of employee {i} is: ₹{total_salary:.2f}")
        total_all_employees += total_salary

    print(f"\nTotal salary of all employees is: ₹{total_all_employees:.2f}")

    
n = int(input("Enter number of employees: "))
calculate_total_salaries(n)



    