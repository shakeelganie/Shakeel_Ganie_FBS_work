# Python Program to Sort a List According to the Length of the Elements within the list.

lst=[]
elements=int(input("Enter the number of elements: "))
for i in range(elements):
    nums=input("Enter the list: ")
    lst.append(nums)

list_sort=sorted(lst, key=len)
print(list_sort)
