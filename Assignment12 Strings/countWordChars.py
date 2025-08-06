# Python Program to Calculate the Number of Words and the Number of Characters Present in a String

string=input("Enter the string: ")
count2=0

str=string.split()
count=len(str)
print(count)

for i in range(len(string)):
    count2+=1
print(count2)

