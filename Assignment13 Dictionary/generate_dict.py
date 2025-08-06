# Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

dict1={}
num=int(input("Enter the number: "))

for x in range(1,num+1):
    
    dict1[x]=x*x
print(dict1)

