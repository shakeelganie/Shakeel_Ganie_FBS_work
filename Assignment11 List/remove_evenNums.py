# Write a program to print list after removing even numbers.

list1=[]

n=int(input("Enter the number of elemnts in a list: "))
for i in range(1,n+1):
    num=int(input("Enter the numbers of a list: "))
    list1.append(num)

new_list=[]
for i in range(len(list1)):
    if list1[i]%2!=0:
        new_list.append(list1[i])
print(f"New list after removing even numbers: {new_list}")