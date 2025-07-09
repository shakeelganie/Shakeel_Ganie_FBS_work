# WAP to print all numbers in a range divisible by a given number.

n=int(input("Enter the number: "))

for i in range(1,n+1):
    if n%i==0:
        print(i)