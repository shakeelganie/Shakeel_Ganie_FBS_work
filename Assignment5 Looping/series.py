''' Write a program to solve the following series :
a. 1! + 2! + 3! + 4! + .....n!
b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
e. x - x2/3 + x3/5 - x4/7 + .... to n terms'''


# a. 1! + 2! + 3! + 4! + .....n!

fact=1
sum=0
n=int(input("Enter the number: "))
for i in range(1,n+1):
    fact*=i
    sum+=fact

print(sum)


# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

sum=0
n=int(input("Enter the number: "))
for i in range(1,n+1):
    ans=n**i
    sum+=ans
print(sum)


# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
n=int(input("Enter the number: "))
ratio=2
sum=0
for i in range(1,n+1):
    a=1*(ratio**(i-1))/(ratio-1)
    sum+=a
print(sum)



# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
n = int(input("Enter the value of a: "))
sum = 0

for i in range(1, 11):
    x= (n ** i) / i
    sum+=x

print(sum)





# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

x=int(input("Enter number"))
n=int(input("Enter number"))
sum=0

for i in range(1,n+1):
    term=(x**i)/(2*i)-1
    if i%2==0:
        sum-=term
    else:
        sum+=term
print(sum)
