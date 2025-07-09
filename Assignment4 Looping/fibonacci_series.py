# WAP to print Fibonacci series upto n.

a=-1
b=1
n=int(input("Enter the number: "))
for i in range(1,n+1):
    c=a+b
    print(c)
    a=b
    b=c