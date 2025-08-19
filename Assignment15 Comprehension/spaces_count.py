# Count the number of spaces in a string (take input from user)
text = input("Enter a string: ")
spaces = len([char for char in text if char == " "])
print("Number of spaces:", spaces)
