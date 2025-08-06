# Python Program to Remove the Given Key from a Dictionary

dict1={}
num=int(input("Enter the number of key-value pairs you want in dictionary: "))
for x in range(num):
    key=input("Enter keys: ")
    dict1[key]=input("Enter values: ")

key=input("Enter the key you want to remove: ")
removed_value=dict1.pop(key)
print(f"The removed key-value is {key}:{removed_value}")
print(f"Dictionary after removing one key value pair: {dict1}")