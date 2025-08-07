# Write a Python program to remove the intersection of a second set with a first set.

# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

# Remove the intersection (common elements) from set1
set1.difference_update(set2)

# Print the updated set1
print("Set1 after removing intersection with set2:", set1)



