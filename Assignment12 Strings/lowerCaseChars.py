# Python Program to count number of lowercase characters in a string.

str1=input("Enter the string: ")
count=0
for i in range(len(str1)):
    x=str1[i].islower()
    count+=x
print(count)