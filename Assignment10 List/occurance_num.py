# Accept a number from user and check if this element is present in the list or not. Also tell how many times it is present in the list.

list1=[]

n=int(input("Enter the number of elemnts in a list: "))
for i in range(n):
    numbers=int(input("Enter the numbers of a list: "))
    list1.append(numbers)

num=int(input("Enter any number of the list: "))
cnt=0
for i in range(len(list1)):
    if num == list1[i]:
        cnt+=1
if cnt>0:
    print(f"the number {num} is present {cnt} times")
else:
    print("The number is not present")


