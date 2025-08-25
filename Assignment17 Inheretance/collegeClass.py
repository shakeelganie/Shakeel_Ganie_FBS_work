'''Create a class College which has collection of students. Add the
following methods :
a. Parameteried constructor for number of students.
b. AddStudent
c. GetStudent
d. RemoveStudent
e. Override __str__ Method'''

# Assuming you already have Student class in StudentClass.py
from StudentClass import Student

class College:
    def __init__(self, collegeName, numStudents=0):
        """Parameterized constructor to initialize college with optional capacity"""
        self.collegeName = collegeName
        self.students = []   # collection of Student objects
        self.capacity = numStudents

    def addStudent(self, student):
        """Add a Student object if capacity allows"""
        if self.capacity == 0 or len(self.students) < self.capacity:
            self.students.append(student)
            print(f"✅ Student {student.name} added successfully.")
        else:
            print("❌ College capacity full! Cannot add more students.")

    def getStudent(self, studentId):
        """Find and return student by studentId"""
        for student in self.students:
            if student.studentId == studentId:
                return student
        print("⚠️ Student not found!")
        return None

    def removeStudent(self, studentId):
        """Remove student by studentId"""
        for student in self.students:
            if student.studentId == studentId:
                self.students.remove(student)
                print(f"🗑️ Student {student.name} removed successfully.")
                return
        print("⚠️ Student not found!")

    def __str__(self):
        """Override string representation for College"""
        details = f"College Name: {self.collegeName}\n"
        details += f"Total Students: {len(self.students)}\n"
        details += "Student List:\n"
        for s in self.students:
            details += f"   {s}\n"  # uses Student.__str__()
        return details

# Assuming Student class looks like: Student(studentId, name, age, percentage)
s1 = Student(101, "Alice", 20, 85)
s2 = Student(102, "Bob", 21, 72)

college = College("ABC Engineering College", numStudents=3)

college.addStudent(s1)
college.addStudent(s2)

print(college)   # Shows all students

# Fetch a student
st = college.getStudent(101)
if st:
    st.display()

# Remove student
college.removeStudent(102)
print(college)
