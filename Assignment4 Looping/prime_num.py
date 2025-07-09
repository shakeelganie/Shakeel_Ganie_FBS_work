# WAP to check if a given number is prime number or not.

n=int(input("Enter the number: "))
for i in range(2,n):
    if n%i==0:
        print("Not a prime number")
        break
else:
    print("prime Number")