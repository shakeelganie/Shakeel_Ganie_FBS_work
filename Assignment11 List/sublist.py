# Python Program to Sort the List According to the Second Element in Sublist

# Sample list of sublists
list_of_sublists = []

# Input: Number of sublists
n = int(input("Enter number of sublists: "))

for i in range(n):
    sublist = []
    print(f"Enter 2 elements for sublist {i+1}:")
    for j in range(2):
        num = int(input(f"  Element {j+1}: "))
        sublist.append(num)
    list_of_sublists.append(sublist)

# Sorting the list based on the second element of each sublist
sorted_list = sorted(list_of_sublists, key=lambda x: x[1])

# Output the result
print("Sorted list based on second element in each sublist:")
print(sorted_list)
