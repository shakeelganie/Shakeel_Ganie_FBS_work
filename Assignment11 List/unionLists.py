# Python Program to Find the Union of two Lists
union_lst=[]
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
    union_lst.append(lst1[i])

for j in range(len(lst2)):
    if lst2[j]!=union_lst:
        union_lst.append(lst2[j])
print(f"Union List of list1 and List2: {union_lst}")
        