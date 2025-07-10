# Write a program to print prime numbers between 1 to 100.

for i in range(1,101):
    for x in range(2,i):
        if i%x==0:
            break
    else:
        print(i)
