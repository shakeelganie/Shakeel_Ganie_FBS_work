# Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary.

str1=input("Enter the string: ")
dict1={}
for s in str1:
    if s in dict1:
        dict1[s]+=1
    else:
        dict1[s]=1
print(dict1)
