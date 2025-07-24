# Write a program to check if given number is Armstrong or not using recursive function.

# Recursive function to count number of digits
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

# Recursive function to calculate Armstrong sum
def armstrong_sum(n, power):
    if n == 0:
        return 0
    digit = n % 10
    return (digit ** power) + armstrong_sum(n // 10, power)

# Main code
num = int(input("Enter a number: "))
num_digits = count_digits(num)
result = armstrong_sum(num, num_digits)

# Check if the number is Armstrong
if result == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")



