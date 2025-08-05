# Python Program to Find the Intersection of Two Lists
 
intersection_list=[]
lst1=[]
elements=int(input("Enter the number of elements: "))
for x in range(elements):
    nums=int(input("Enter the list: "))
    lst1.append(nums)

lst2=[]
elements=int(input("Enter the number of elements: "))
for y in range(elements):
    nums=int(input("Enter the list: "))
    lst2.append(nums)

for i in range(len(lst1)):
    for j in range(len(lst2)):
        if lst1[i]==lst2[j]:
            intersection_list.append(lst1[i])

print(intersection_list)