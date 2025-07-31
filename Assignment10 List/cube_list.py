# Write a program to create a new list from existing list which contains cube of each number of list.

list1=[]

n=int(input("Enter the number of elemnts in a list: "))
for i in range(1,n+1):
    num=int(input("Enter the numbers of a list: "))
    list1.append(num)

new_list=[]
for i in range(len(list1)):
    cube=list1[i]**3
    new_list.append(cube)
print(f"The cube of numbers in a new_list is: {new_list}")
