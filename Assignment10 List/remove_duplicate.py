# Write a program to remove duplicates from the list.

list1=[]
n=int(input("Enter the number of elemnts in a list: "))
for i in range(1,n+1):
    num=int(input("Enter the numbers of a list: "))
    list1.append(num)

list2=[]
for i in range(len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
print(f"Original list:{list1}")
print(f"list after removing duplicates:{list2}")