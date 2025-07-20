# Hollow right angled triangle with pattren of numbers

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        # Print number if it's the first, last in the row, or the last row
        if j == 1 or j == i or i == n:
            print(j, end=' ')
        else:
            print(' ', end=' ')
    print()
