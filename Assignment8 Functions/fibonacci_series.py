# Write a program to find print the following Fibonacci series using functions:
# 1 1 2 3 5 8 n terms

def fibonacci_series():
    n=int(input("Enter the number: "))
    a=1
    b=0
    
    for i in range(1,n+1):
        c=a+b
        print(c)
        a=b
        b=c
fibonacci_series()
