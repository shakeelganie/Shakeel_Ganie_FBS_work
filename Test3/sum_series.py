# sum of series 
sum=0
fact=1
n=int(input("Enter the number: "))
for i in range(1,n+1):
    fact*=i/i
    sum+=fact
    print(sum)
