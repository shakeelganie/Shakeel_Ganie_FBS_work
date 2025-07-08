# calculate the cost of painting of interior of a building with four equal sized walls

side1=int(input("enter the lenght of one side of a wall: "))
height=int(input("Enter the height of a wall"))
cost=int(input("Enter the cost of paintaing: "))
area=4*side1*height
total_cost=area*cost
print("Total cost: ",total_cost)