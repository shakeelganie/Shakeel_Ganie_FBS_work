# Write a program to find sum of following series using recursive functions:

# 1! + 2! + 3! + 4! +..... + n!
# Note : For fact and sum two recursive functions

# Recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Recursive function to calculate sum of series 1! + 2! + ... + n!
def sum_of_series(n):
    if n == 1:
        return factorial(1)
    return factorial(n) + sum_of_series(n - 1)

# Taking input from user
n = int(input("Enter the value of n: "))

# Calling the function and displaying the result
result = sum_of_series(n)
print("Sum of the series 1! + 2! + ... +", n, "! =", result)

