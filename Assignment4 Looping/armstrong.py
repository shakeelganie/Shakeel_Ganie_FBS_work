# WAP to print Armstrong number within a given range

num=int(input("Enter the num: "))
temp=num
count=0

while num!=0:
    a=num%10
    num=num//10
    count+=1

num=temp
sum=0

while num!=0:
    a=num%10
    num=num//10
    #num//=10   alternative option
    sum=sum+(a**count)

if sum==temp:
    print("This is Armstrong Number")
else:
    print("This is not an armstrong number")