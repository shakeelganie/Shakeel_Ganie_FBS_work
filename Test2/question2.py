# calculate the three digit number, which has firt digit double of its second digit and half of its third digit.

num=int(input("Enter the three digit number: "))

a=num%10
b=num//10
c=b%10
d=b//10
a=2*c
a=d//2

print(a,c,d)
