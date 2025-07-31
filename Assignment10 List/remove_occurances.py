# Write a program to remove all occurrences of a given element in the list.

list1=[]
n=int(input("Enter the number of elemnts in a list: "))
for i in range(1,n+1):
    num=int(input("Enter the numbers of a list: "))
    list1.append(num)
c=0
number=int(input("Enter the number: "))
for i in range(len(list1)):
    if list1[i]==number:
        c+=1
for i in range(c):
    list1.remove(number)
print(f"List after removing all the occurances of a given number: {list1}")
