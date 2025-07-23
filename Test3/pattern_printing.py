rows = 5
cols = 4

for i in range(rows):
    for j in range(cols):
        if i % 2 == 0:  # rows: 0, 2, 4 (1st, 3rd, 5th)
            if j == 0 or j == cols - 1:
                print("1", end=" ")
            else:
                print("0", end=" ")
        else:  # rows: 1, 3 (2nd, 4th)
            if j == 0 or j == cols - 1:
                print("0", end=" ")
            else:
                print("1", end=" ")
    print()
