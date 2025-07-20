# Pyramid Patterns in Python with Alphabet

n = 5  # number of rows

for i in range(n):
    letters = 2 * i + 1  # Number of letters in the row (1, 3, 5, ...)
    spaces = n - i - 1   # Spaces before the letters to center the row

    # Print leading spaces
    print("  " * spaces, end='')

    # Print letters from 'A' onwards
    for j in range(letters):
        print(chr(65 + j), end=' ')
    
    print()
