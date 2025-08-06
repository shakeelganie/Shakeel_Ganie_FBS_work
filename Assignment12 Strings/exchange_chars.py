# Python Program to Form a New String where the First Character and the Last Character have been Exchanged

string=input("Enter the string: ")
first_char=(string[0])
last_char=(string[-1])
middle_char=string[1:-1]
new_string=last_char+middle_char+first_char
print(new_string)

