# printing pyramid pattern of numbers

n = 5

for i in range(1, n + 1):
    print("  " * (n - i), end="")  # Leading spaces

    # Increasing part
    num = i
    for j in range(i):
        print(num, end=" ")
        num += 1

    # Decreasing part
    num -= 2
    for j in range(i - 1):
        print(num, end=" ")
        num -= 1

    print()
