# Write a program to check whether a number is prime or not using recursion.

# Recursive function to check for prime
def is_prime(n, i=2):
    if n <= 1:
        return False
    if i == n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)

# Main code
num = int(input("Enter a number: "))

if is_prime(num):
    print(num, "is a Prime number.")
else:
    print(num, "is NOT a Prime number.")
