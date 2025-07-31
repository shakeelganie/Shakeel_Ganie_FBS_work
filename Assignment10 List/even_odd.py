# Write a program of having n number of elements in the list and find out even and odd elements in that list and then create two separate lists which will have even elements and other will have odd elements.

list1=[]

n=int(input("Enter the number of elements in a list: "))
for i in range(n):
    elements=int(input("Enter the number of elements in a list: "))
    list1.append(elements)
print(f"Given List: {list1}")

even_list=[]
odd_list=[]
for i in range(len(list1)):
    if list1[i]%2==0:
        even_list.append(list1[i])
    else:
        odd_list.append(list1[i])
print(f"Even list: {even_list}")
print(f"Odd list: {odd_list}")

