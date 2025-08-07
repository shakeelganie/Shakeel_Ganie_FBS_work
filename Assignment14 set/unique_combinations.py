# Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number.

# Input list of numbers and target value
numbers = [1, 2, -1, 0, -2, 1, -1, 3]
target = 2

# Set to store unique triplets
unique_combinations = set()

# Get length of the list
n = len(numbers)

# Iterate through all triplets
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            # Check if the sum equals the target
            if numbers[i] + numbers[j] + numbers[k] == target:
                # Sort and store the combination as a tuple to ensure uniqueness
                triplet = tuple(sorted([numbers[i], numbers[j], numbers[k]]))
                unique_combinations.add(triplet)

# Print the result
print(f"Unique combinations of 3 numbers that sum to {target}:")
for combo in unique_combinations:
    print(combo)

