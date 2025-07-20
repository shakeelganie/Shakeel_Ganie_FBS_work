# Pyramid pattern with numbers

n = 4
for i in range(n):
    print(" " * (n - i - 1), end='')  # spacing
    for j in range(i + 1):
        if j == 0 or j == i:
            print("1", end=' ')
        else:
            print(i, end=' ')
    print()

