# Python Program to Add a Key-Value Pair to the Dictionary

dict1={}
num=int(input("Enter how many key-values pairs you want to run: "))
for i in range(num):
    key=int(input("Enter the key: "))
    value=input("Enter the value: ")
    dict1[key]=value

dict1[5]="E"
print(dict1)
