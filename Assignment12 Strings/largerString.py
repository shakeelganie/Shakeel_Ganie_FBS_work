# Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions

string1=input("Enter string1: ")
string2=input("Enter string2: ")

len1=len(string1)
len2=len(string2)
if len1>len2:
    print(f"String1 is larger: {string1}")
else:
    print(f"String2 is larger: {string2}")
