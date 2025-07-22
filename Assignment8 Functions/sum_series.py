#  3. Write a program to find sum of following series using functions :
#  a. 1+ 2 + 3 + 4+..... + n
#  b. 1!+ 2! + 3! + 4!+..... + n!
#  c. 1^1 + 2^2 + 3^3+ ...... n^n

def sum_num(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total
    
n=int(input("Enter the number: "))
num=sum_num(n)
print(num)


def sum_factorial(n):
    fact=1
    sum=0
    for i in range(1,n+1):
        fact*=i
        sum+=fact
    return sum

n=int(input("Enter the number: "))
num=sum_factorial(n)
print(num)


def sum_pow(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i ** i
    return total_sum
    


# Example usage:
n=int(input("Enter the number: "))
result = sum_pow(n)
print(f"The sum of the series up to n={n} is: {result}")

