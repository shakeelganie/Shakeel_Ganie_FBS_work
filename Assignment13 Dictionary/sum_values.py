# Python Program to Sum All the Items in a Dictionary
total=0
dict1={}
for i in range(1,4):
    key=int(input("Enter keys: "))
    value=int(input("Enter values: "))
    dict1[key]=value
for j in dict1:
    total+=dict1[j]
print(total)


