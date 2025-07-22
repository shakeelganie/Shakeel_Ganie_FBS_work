#  Write a program to check if entered number is a palindrome or not
def palindromeNum(num):
    temp=num
    reverse=0
    while num>0:
        digit=num%10
        reverse=reverse*10+digit
        num=num//10
    return reverse==temp

num=int(input("Enter number:"))
if palindromeNum(num):
    print("It is a palindrome")
else:
    print("It is not a palindrome")

    
