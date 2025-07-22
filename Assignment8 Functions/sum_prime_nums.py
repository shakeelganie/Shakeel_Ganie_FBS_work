#  Sum of all prime numbers between 1 to n

def sumPrimeNums(n):
    sum=0
    for num in range(2,n+1):
        for i in range(2,num):
            if num%2==0:
                break
        else:
            sum+=num
    return sum
num=int(input("Enter num: "))
result=sumPrimeNums(num)
print(result)