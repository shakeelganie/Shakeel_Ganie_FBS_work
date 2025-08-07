# Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.

# Sample list of strings
string_list = ["apple banana apple", "banana orange", "apple orange banana"]

# Step 1: Create a set for unique words
unique_words = set()

# Step 2: Create a dictionary to store word frequencies
word_freq = {}

# Step 3: Loop through each string in the list
for sentence in string_list:
    words = sentence.split()  # Split sentence into words
    for word in words:
        unique_words.add(word)  # Add to set of unique words
        word_freq[word] = word_freq.get(word, 0) + 1  # Count frequency

# Step 4: Display the results
print("Unique words:", unique_words)
print("Word frequencies:")
for word in unique_words:
    print(f"{word}: {word_freq[word]}")



