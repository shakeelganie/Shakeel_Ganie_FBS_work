#  Calculate the percentage of the marks of a student based on 5 subjects

m1=int(input("Enter the marks of 1st subject: "))
m2=int(input("Enter the marks of 2st subject: "))
m3=int(input("Enter the marks of 3st subject: "))
m4=int(input("Enter the marks of 4st subject: "))
m5=int(input("Enter the marks of 5st subject: "))

total_marks=m1+m2+m3+m4+m5
print("Total marks of a student of five subjects is: ", total_marks)
max_marks=int(input("Enter the maximum marks: "))
percentage=(total_marks/max_marks)*100
print("The percentage of marks of five subjects of a student is: ", percentage,"%")