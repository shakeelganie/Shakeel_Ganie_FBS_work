# Write a program to input all sides of a triangle and check whether triangle is valid or not

side1= int(input("Enter side1 of a triangle: "))
side2= int(input("Enter side2 of a triangle: "))
side3= int(input("Enter side3 of a triangle: "))

if side1+side2>side3 or side2+side3>side1 or side3+side1>side2:
    print("Triangle is valid")
else:
    print("Triangle is invalid")