# Sum of 3 digit numbers

num=int(input("Enter the three digit number: "))

a=num%10
b=num//10
c=b%10
d=b//10
ans=a+c+d
print("The sum of three digit numbsrs is: ",ans)