#  Write a program to calculate area of circle

def circleArea(r):
    area=3.14*r*r
    return area
radius=float(input("Enter the radius of the circle: "))
total_area=circleArea(radius)
print(round(total_area,2))