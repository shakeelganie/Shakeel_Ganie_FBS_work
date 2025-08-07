# Write a Python program to find all the anagrams and group them together from a given list of strings.

from collections import defaultdict

# Sample list of strings
words = ["bat", "tab", "tap", "pat", "cat", "act", "tac", "dog", "god"]

# Dictionary to hold grouped anagrams
anagram_groups = defaultdict(list)

# Iterate over each word
for word in words:
    # Sort the word and use it as the key
    sorted_word = ''.join(sorted(word))
    anagram_groups[sorted_word].append(word)

# Display grouped anagrams
print("Grouped Anagrams:")
for group in anagram_groups.values():
    print(group)
