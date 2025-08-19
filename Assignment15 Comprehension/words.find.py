# Find all of the words in a string that are less than 5 letters (take input from user)

text = input("Enter a string: ")

# Split the string into words
words = text.split()

# Find words with length less than 5
short_words = [word for word in words if len(word) < 5]

print("Words with less than 5 letters are:", short_words)
