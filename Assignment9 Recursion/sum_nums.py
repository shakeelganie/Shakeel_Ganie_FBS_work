# Write a program to find sum of n numbers using recursion.

# Recursive function to find sum of n numbers
def recursive_sum(n):
    if n == 1:
        return 1
    return n + recursive_sum(n - 1)

# Main code
num = int(input("Enter a number: "))
if num <= 0:
    print("Please enter a positive integer.")
else:
    total = recursive_sum(num)
    print("Sum of first", num, "natural numbers is:", total)
