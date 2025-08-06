# Python Program to Concatenate Two Dictionaries Into One

dict1={}
nums1=int(input("Enter the number of pairs you want to run: "))
for i in range(nums1):
    key=int(input("Enter keys: "))
    value=input("Enter values: ")
    dict1[key]=value

dict2={}
nums2=int(input("Enter the number of pairs you want to run: "))
for j in range(nums2):
    key=int(input("Enter keys: "))
    value=input("Enter values: ")
    dict2[key]=value

dict1.update(dict2)
print(dict1)