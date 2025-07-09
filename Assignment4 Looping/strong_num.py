# WAP to check if given number Strong Number.

num=int(input("Enter the number: "))
temp=num

sum_fact=0
while num!=0:
    a=num%10
    
    fact=1
    for i in range(1,a+1):
        fact*=i
    sum_fact+=fact
    num=num//10


if sum_fact==temp:
    print("Strong number")
else:
    print("Not a strong number")





    







