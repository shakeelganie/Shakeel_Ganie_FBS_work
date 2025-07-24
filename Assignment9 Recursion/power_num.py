# Write a program to calculate the m to the power n using recursion.

# Recursive function to calculate m^n
def power(m, n):
    if n == 0:
        return 1
    return m * power(m, n - 1)

# Main code
m = int(input("Enter the base (m): "))
n = int(input("Enter the exponent (n): "))

result = power(m, n)
print(f"{m} to the power {n} is: {result}")
