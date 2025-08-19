# Remove all of the vowels in a string (take input from user)
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = "".join([ch for ch in text if ch not in vowels])
print("String without vowels:", result)

