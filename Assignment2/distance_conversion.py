# convert the distance given in feet and inches into meter and centimeter

feet=int(input("Enter the number of feets: "))
inches=int(input("Enter the number of inches: "))

meter= feet*0.3048
centimeter=inches*2.54

print("feet into meters: ",round(meter,2),"m")
print("Inches into centimeter: ",round(centimeter,2),"cms")