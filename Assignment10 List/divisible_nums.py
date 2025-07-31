#  Write a program to print all numbers which are divisible by m and n in the list.


lst=[]
elements=int(input("Enter the number of elements in the list: "))
for i in range(elements):
    nums=int(input("Enter the numbers in  list: "))
    lst.append(nums)
print(lst)
m=int(input("Enter number: "))
n=int(input("Enter number: "))
new_list=[]
for i in range(len(lst)):
    if lst[i]%m==0 and lst[i]%n==0:
        new_list.append(lst[i])
print(new_list)




