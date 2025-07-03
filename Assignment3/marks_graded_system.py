# Input 5 subject marks from user and display grade(eg.First class,Second class ..)

# Input marks for 5 subjects
mark1 = float(input("Enter marks for subject 1: "))
mark2 = float(input("Enter marks for subject 2: "))
mark3 = float(input("Enter marks for subject 3: "))
mark4 = float(input("Enter marks for subject 4: "))
mark5 = float(input("Enter marks for subject 5: "))

# Calculate total and average
total = mark1 + mark2 + mark3 + mark4 + mark5
average = total / 5

# Determine grade
if average >= 60:
    grade = "First Class"
elif average >= 50:
    grade = "Second Class"
elif average >= 40:
    grade = "Pass Class"
else:
    grade = "Fail"

# Display result
print("\nTotal Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)
