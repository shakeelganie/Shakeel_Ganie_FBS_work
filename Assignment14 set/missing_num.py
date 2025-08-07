# Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set.

# Define the two sets of numbers
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8}

# Find numbers in set1 that are missing in set2
missing_in_set2 = set1 - set2

# Find numbers in set2 that are missing in set1
missing_in_set1 = set2 - set1

# Display the results
print("Numbers present in Set 1 but missing in Set 2:", missing_in_set2)
print("Numbers present in Set 2 but missing in Set 1:", missing_in_set1)
