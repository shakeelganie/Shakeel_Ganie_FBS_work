#  Write a program find reverse of a number

def reverseNum(n):
    reverse=0
    while n>0:
        digits=n%10
        reverse=reverse*10+digits
        n=n//10
    return reverse
n=int(input("Enter the number: "))
result=reverseNum(n)
print(result)