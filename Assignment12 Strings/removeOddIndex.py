# Python Program to Remove the Characters of Odd Index Values in a String
string=input("Enter the string: ")
new_string=""
for i in range(len(string)):
    if i%2==0:
        new_string+=string[i]
print(new_string)