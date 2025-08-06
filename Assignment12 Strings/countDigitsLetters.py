# Python Program to count number of digits and letters in a string.

string=input("Enter the string: ")

alpha=0
nums=0


for i in string:
    if i.isalpha():
        alpha+=1
        
    elif i.isnumeric():
        nums+=1
    
print(f"Alphabets are: {alpha}")
print(f"Numbers are: {nums}")

