# Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit.

# Find numbers from 1 to 1000 divisible by any single digit (2-9)
numbers = [x for x in range(1, 1001) if any(x % d == 0 for d in range(2, 10))]

print(numbers)

