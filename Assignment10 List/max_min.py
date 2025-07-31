# Write a program to find maximum and minimum element in a list.

list1=[]

n=int(input("Enter the number of elemnts in a list: "))
for i in range(1,n+1):
    num=int(input("Enter the numbers of a list: "))
    list1.append(num)

large=list1[0]                       # max number
for i in range(1,len(list1)):
    if large<list1[i]:
        large=list1[i]
print(f"largest number is {large}")


small=list1[0]                      # min number
for i in range(len(list1)):
    if small>list1[i]:
        small=list1[i]
print(f"smallest number is {small}")
