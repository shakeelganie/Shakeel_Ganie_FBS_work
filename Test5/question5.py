'''Python Program to Find the Union of two Lists without
using set concept.'''

# Input lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

union_list = []

# Add elements from list1
for item in list1:
    if item not in union_list:
        union_list.append(item)

# Add elements from list2
for item in list2:
    if item not in union_list:
        union_list.append(item)

print("Union of two lists:", union_list)
