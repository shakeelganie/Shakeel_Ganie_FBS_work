# Python Program to Put Even and Odd elements of a List into two Different Lists
lst=[]
elements=int(input("Enter the number of elements: "))
for i in range(elements):
    nums=int(input("Enter the numbers for a list: "))
    lst.append(nums)

even=[]
odd=[]
for i in range(len(lst)):
    if lst[i]%2==0:
        even.append(lst[i])
    if lst[i]%2!=0:
        odd.append(lst[i])
print(f"Evem Numbers list: {even}")
print((f"Odd Numbers list: {odd}"))


