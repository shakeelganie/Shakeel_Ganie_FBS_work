# Python Program to Merge Two Lists and Sort it

# Program to merge two lists and sort the result

# Input: Two lists
list1 = []
list2 = []

# Taking input for first list
n1 = int(input("Enter number of elements in first list: "))
for i in range(n1):
    num = int(input(f"Enter element {i+1} of first list: "))
    list1.append(num)

# Taking input for second list
n2 = int(input("Enter number of elements in second list: "))
for i in range(n2):
    num = int(input(f"Enter element {i+1} of second list: "))
    list2.append(num)

# Merging the lists
merged_list = list1 + list2

# Sorting the merged list
merged_list.sort()

# Output the sorted merged list
print("The merged and sorted list is:", merged_list)
