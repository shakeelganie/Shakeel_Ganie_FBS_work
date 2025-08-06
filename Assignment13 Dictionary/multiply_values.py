# Python Program to Multiply All the Items in a Dictionary

multiply=1
dict1={}
for i in range(1,4):
    key=int(input("Enter keys: "))
    value=int(input("Enter values: "))
    dict1[key]=value
for j in dict1:
    multiply*=dict1[j]
print(multiply)