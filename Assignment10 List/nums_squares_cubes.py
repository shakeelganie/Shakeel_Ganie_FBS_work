# Write a program to create three lists of numbers, their squares and cubes.

lst=[]
elements=int(input("Enter the numbers of elements in a list: "))
for i in range(elements):
    nums=int(input("Enter the numbers in a list: "))
    lst.append(nums)
print(f"Numbers: {lst}")

squares=[]
for i in range(len(lst)):
    squares.append(lst[i]**2)
print(f"Squares: {squares}")

cubes=[]
for i in range(len(lst)):
    cubes.append(lst[i]**3)
print(f"Cubes: {cubes}")
