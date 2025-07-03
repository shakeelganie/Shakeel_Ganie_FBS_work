# Write a program to input angles of a triangle and check whether triangle is valid or not.

angle1= int(input("Enter the angle1 of a triangle: "))
angle2= int(input("Enter the angle2 of a triangle: "))
angle3= int(input("Enter the angle3 of a triangle: "))

if (angle1+angle2+angle3)==180:
    print("Triangle is valid")
else:
    print("Invalid triangle")