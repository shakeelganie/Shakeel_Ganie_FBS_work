# Write a program to reverse a given number using recursive function.

# Recursive function to reverse a number
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    remainder = n % 10
    rev = rev * 10 + remainder
    return reverse_number(n // 10, rev)

# Main code
num = int(input("Enter a number: "))
reversed_num = reverse_number(num)

print("Reversed number is:", reversed_num)
