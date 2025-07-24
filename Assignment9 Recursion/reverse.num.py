# Write a program to reverse a number using recursion.

# Recursive function to reverse a number
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    rev = rev * 10 + (n % 10)
    return reverse_number(n // 10, rev)

# Main code
num = int(input("Enter a number: "))

# Handle negative numbers if needed
is_negative = num < 0
num = abs(num)

reversed_num = reverse_number(num)

if is_negative:
    reversed_num = -reversed_num

print("Reversed number is:", reversed_num)
