#  Write a program to calculate area of rectangle

def areaRectangle(l,b):
    area=l*b
    return area
length=int(input("Enter the length of a rectangle: "))
breadth=int(input("Enter the breadth of a rectangle: "))
total_area=areaRectangle(length,breadth)
print("total area of the rectangle is: ",total_area)