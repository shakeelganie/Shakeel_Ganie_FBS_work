#   Find the roots of quadract equation

a= int(input("Enter the num a: "))
b= int(input("Enter the num b: "))
c= int(input("Enter the num c: "))

ans=(b*b)-(4*a*c)
ans=ans**0.5
root1=(-b+ans)/2*a
root2=(-b-ans)/2*a
print("Root1: ",root1)
print("Root2: ",root2)