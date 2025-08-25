'''Create a class MedicalStudent inherited from Student with following
:

i. Data members :Specialization
ii. MarksOfInternship
b. Add the following methods :
i. Parameterized constructor
ii. Display
iii. Accept
iv. override Method CalculateRank
v. Override __str__ Method'''
from StudentClass import Student
class MedicalStudent(Student):
    def __init__(self, studentId=1234, name="", age=0, percentage=0,specialization="", marksInternship=0.0):
        super().__init__(studentId, name, age, percentage)
        self.specialization = specialization
        self.marksinternship=marksInternship

    def display(self):
        """Override display to include MedicalStudent details"""
        super().display()
        print(f"Specialization: {self.specialization}")
        print(f"Internship Marks: {self.marksinternship}")

    def accept(self):
        self.specialization = input("Enter specialization: ")
        self.marksinternship = float(input("Enter internship marks: "))

    
    def calculateRank(self):
        """Override: Rank depends on percentage + internship marks"""
        total_score = (self.percentage + self.marksinternship) / 2
        if total_score >= 85:
            self.rank = "Distinction"
        elif total_score >= 70:
            self.rank = "Merit"
        else:
            self.rank = "Pass"

    def __str__(self):
    #Override string representation
        return (f"Medical Student [ID={self.studentId}, Name={self.name}, "
                f"Age={self.age}, Percentage={self.percentage}, "
                f"Specialization={self.specialization}, "
                f"Internship Marks={self.marksinternship}, Rank={self.rank}]")

        
        
m1 = MedicalStudent(15467,"Alice", 101, 78, "Cardiology", 90)
m1.calculateRank()
m1.display()

print(m1)   # Uses __str__ method
