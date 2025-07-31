# Write a program to find the second largest element in the list.

list1=[]             # Create an empty list

n=int(input("Enter the number of elemnts in a list: "))
for i in range(1,n+1):
    num=int(input("Enter the numbers of a list: "))
    list1.append(num)    # fill the list1

large=list1[0]                    #largest number
for i in range(1,len(list1)):
    if large<list1[i]:
        large=list1[i]
print(large)

second_largest=0                 # second largest number
for i in range(1,len(list1)):
    if list1[i]!=large:
        if second_largest<list1[i]:
            second_largest=list1[i]
print(f"the second latgest number is: {second_largest}")
