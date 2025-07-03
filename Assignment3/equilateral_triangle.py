# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.


side1=int(input("Enter the length of side1: "))
side2=int(input("Enter the length of side2: "))
side3=int(input("Enter the length of side3: "))

if side1==side2==side3:
    print("It is an equilateral triangle")
elif side1==side2 or side2==side3 or side3==side1:
    print("It is an isosceles triangle")
elif side1 != side2 != side3:
    print("It is a scalene triangle")
else:
    print("It is a wrong input")