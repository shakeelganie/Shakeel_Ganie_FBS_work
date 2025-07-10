'''Enter number of students from user. For those many students accept marks of 5
subject marks from user and calculate percentage. Display all percentage and
average percentage of students.'''

# Accept number of students
num_students = int(input("Enter the number of students: "))

# List to store each student's percentage
percentages = []

# Loop over each student
for student in range(1, num_students + 1):
    print(f"\nEnter marks for Student {student}:")
    total_marks = 0

    # Loop for 5 subjects
    for subject in range(1, 6):
        mark = float(input(f"  Enter mark for Subject {subject}: "))
        total_marks += mark

    # Calculate percentage for this student
    percentage = (total_marks / 500) * 100
    percentages.append(percentage)

# Display each student's percentage
print("\n--- Students' Percentages ---")
for index, perc in enumerate(percentages, start=1):
    print(f"Student {index}: {perc:.2f}%")

# Calculate average percentage
average_percentage = sum(percentages) / num_students
print(f"\nAverage Percentage of All Students: {average_percentage:.2f}%")