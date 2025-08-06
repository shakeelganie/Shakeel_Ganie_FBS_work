# Python Program to Replace all Occurrences of ‘a’ with $ in a String

# Input string
original_string = input("Enter a non-empty string: ")

# Input index to remove
n = int(input("Enter the index to remove: "))

# Check if index is valid
if n < 0 or n >= len(original_string):
    print("Invalid index!")
else:
    # Remove the nth character
    new_string = ""
    for i in range(len(original_string)):
        if i != n:
            new_string += original_string[i]
    
    # Print result
    print("String after removing character at index", n, ":", new_string)
