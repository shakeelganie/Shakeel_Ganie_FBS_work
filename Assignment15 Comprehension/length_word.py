# Use a dictionary comprehension to count the length of each word in a sentence (take input from user)

# Take input from user
text = input("Enter a sentence: ")

# Dictionary comprehension to count length of each word
word_lengths = {word: len(word) for word in text.split()}

print("Word lengths:", word_lengths)

