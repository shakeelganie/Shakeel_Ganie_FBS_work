# Write a program to create a duplicate of an existing list. It should not point to same list.

list1=[]

n=int(input("Enter the number of elemnts in a list: "))
for i in range(1,n+1):
    num=int(input("Enter the numbers of a list: "))
    list1.append(num)
print(f"Existing list: {list1}")
duplicate_list=[]
for i in range(len(list1)):
    duplicate_list.append(list1[i])
print(f"Duplicate list : {duplicate_list}")
