#  Pyramid with printing stars


rows = 5
cols = 9

for i in range(1, rows + 1):
    stars = 2 * i - 1              # Number of stars for current row
    spaces = (cols - stars) // 2   # Spaces on each side
    print(" " * spaces + "*" * stars + " " * spaces)

