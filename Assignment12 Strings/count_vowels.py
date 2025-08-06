# Python Program to Count the Number of Vowels in a String
count=0
string=input("Enter the string: ")
vowels=("a", "e", "i", "o", "u")
for i in range(len(vowels)):
    if vowels[i] in string:
        nums=string.count(vowels[i])
        count+=nums
print(count)

