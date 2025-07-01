# calculate the cost of painting of two same buildings walls which is in square shape (both interior and exterior). in python code

side_length = int(input("Enter the lenght of a side: "))
interior_cost = int(input("Enter the interior cost per sq ft: "))
exterior_cost = int(input("Enter the exterior cost per sq ft: "))

area_per_wall = side_length * side_length
total_area = 4 * area_per_wall
interior_cost = total_area * interior_cost
exterior_cost = total_area * exterior_cost
total_cost = 2 * (interior_cost + exterior_cost)



print("The total cost of painting the two buildings is: $",total_cost)