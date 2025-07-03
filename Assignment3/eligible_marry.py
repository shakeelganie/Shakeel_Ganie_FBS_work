# Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

male_age=int(input("Enter the age of a male: "))
female_age=int(input("Enter the age of a female: "))

if male_age>=21:
    print("Male is eligible to marry")
else:
    print("Male is not eligible")
if female_age>=18:
    print("Female is eligible to marry")
else:
    print("Female is not eligible")
