# Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set.

# Input list of numbers
nums = [3, 5, -10, -20, 7, 5, 3, -10]

# Convert list to set to remove duplicates
unique_nums = set(nums)

# Check if there are at least 2 unique numbers
if len(unique_nums) < 2:
    print("Not enough unique numbers to form a pair.")
else:
    # Convert set back to a sorted list
    sorted_nums = sorted(unique_nums)

    # Get two largest and two smallest numbers
    max1 = sorted_nums[-1]
    max2 = sorted_nums[-2]

    min1 = sorted_nums[0]
    min2 = sorted_nums[1]

    # Calculate both possible max products
    product_max = max1 * max2
    product_min = min1 * min2

    # Compare and print the pair with the maximum product
    if product_max >= product_min:
        print(f"The pair with the maximum product is: ({max1}, {max2})")
        print(f"The maximum product is: {product_max}")
    else:
        print(f"The pair with the maximum product is: ({min1}, {min2})")
        print(f"The maximum product is: {product_min}")

