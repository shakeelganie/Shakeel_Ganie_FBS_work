#  mirrored V-shaped pattern with numbers

n = 5
for i in range(1, n + 1):
    # Left side increasing
    for j in range(1, i + 1):
        print(j, end=" ")

    # Middle spaces
    spaces = (n - i) * 4  # Each space group = 2 spaces × 2 (for width of numbers and gap)
    print(" " * spaces, end="")

    # Right side decreasing
    for j in range(i, 0, -1):
        print(j, end=" ")

    print()
