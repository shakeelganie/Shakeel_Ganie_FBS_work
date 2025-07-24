# Write a program to print Fibonacci series using recursion.

# Recursive function to find nth Fibonacci number
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Main code to print Fibonacci series
num = int(input("Enter how many terms you want: "))

print("Fibonacci series:")
for i in range(num):
    print(fibonacci(i), end=' ')
