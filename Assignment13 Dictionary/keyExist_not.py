# Python Program to Check if a Given Key Exists in a Dictionary or Not

dict1={}
nums=int(input("Enter number of key values pairs you want to run: "))
for i in range(nums):
    keys=input("Enter keys: ")
    values=input("Enter values: ")
    dict1[keys]=values
print(f"Your dictionary: {dict1}")


key=input("Enter the key you want to check if it exists in dictionary: ")
if key in dict1:
    print("Yes Exists")
else:
    print("Not Exists")