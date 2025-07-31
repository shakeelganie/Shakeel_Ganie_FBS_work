# Write a program to find sum of all elements of list
list1=[]

n=int(input("Enter the number of elemnts in a list: "))
for i in range(1,n):
    num=int(input("Enter the numbers of a list: "))
    list1.append(num)
sum=0
for i in range(len(list1)):
    sum+=list1[i]
print(sum)

