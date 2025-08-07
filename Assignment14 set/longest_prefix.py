# Write a Python program to find the longest common prefix of all strings. Use the Python set.

# Sample list of strings
strs = ["flower", "flow", "flight"]

# Edge case: empty list
if not strs:
    print("No strings provided.")
else:
    # Find the shortest string (prefix can't be longer than this)
    shortest = min(strs, key=len)
    prefix = ""

    # Iterate character by character
    for i in range(len(shortest)):
        # Collect the i-th character from each string into a set
        chars_at_i = {s[i] for s in strs}

        # If all characters are same at position i, add to prefix
        if len(chars_at_i) == 1:
            prefix += chars_at_i.pop()  # Only one element in set
        else:
            break  # Mismatch found, stop checking

    # Output the result
    print("Longest common prefix:", prefix if prefix else "None")

