# Python Program to Find the Second Largest Number in a List Using Bubble Sort
def bubbleSort(lst):
    for i in range(1,len(lst)):
        for j in range(len(lst)-i):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst

lst=[4,2,6,8,5,3,9,5]
sorted_list = bubbleSort(lst)

largest = sorted_list[-1]
second_largest = None

for i in range(len(sorted_list) - 2, -1, -1):  # start from second last element
    if sorted_list[i] != largest:
        second_largest = sorted_list[i]
        break

# Output
if second_largest is not None:
    print("Second largest number is:", second_largest)
else:
    print("All elements are equal. No second largest number.")


