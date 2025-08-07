# Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

# Sample list and target sum
numbers = [2, 4, 3, 5, 7, 8, 1]
target_sum = int(input("Enter the target sum: "))

# Initialize a list to store pairs
pairs = []

# Find all pairs whose sum equals target_sum
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target_sum:
            pairs.append((numbers[i], numbers[j]))

# Display the result
print("Pairs with sum", target_sum, "are:", pairs)

