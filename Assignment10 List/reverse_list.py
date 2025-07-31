# Write a program to reverse the list.

list1=[]

n=int(input("Enter the number of elemnts in a list: "))
for i in range(1,n+1):
    num=int(input("Enter the numbers of a list: "))
    list1.append(num)
print(f"original list given by user: {list1}")
print(f"Reverse order of th list: {list1[::-1]}")    
