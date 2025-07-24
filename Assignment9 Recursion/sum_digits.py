# Write a program to find sum of digits using recursion.

# Recursive function to calculate sum of digits
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

# Main code
num = int(input("Enter a number: "))

# Handle negative numbers
num = abs(num)

result = sum_of_digits(num)
print("Sum of digits is:", result)
