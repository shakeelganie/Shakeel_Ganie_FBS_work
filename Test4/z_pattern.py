n = int(input("Enter the size of the Z pattern: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1:
            print("*", end="")
        elif j == n - i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


