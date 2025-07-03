# Write a program to check if given 3 digit number is a palindrome or not.

num=int(input("Enter the number: "))
temp=num
reverse=0

while num>0:
    digit=num%10
    reverse=(reverse*10)+digit
    num=num//10


if temp==reverse:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
