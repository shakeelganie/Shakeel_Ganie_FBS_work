'''Create a derived class from Student as EnggStudent with :
a. Data members as :
i. Branch
ii. InternalMarks
b. Add the following methods :
i. Parameterized constructor
ii. Display
iii. Accept
iv. override Method CalculateRank
v. Override __str__ Method'''


from StudentClass import Student
class EnggStudent(Student):
    def __init__(self, studentId=1234, name="", age=0, percentage=0, branch="",internalmarks=0):
        super().__init__(studentId, name, age, percentage)
        self.branch=branch
        self.internalmarks=internalmarks

    def display(self):
        print(f"Branch: {self.branch}")
        print(f"Internal marks: {self.internalmarks}")

    def accept(self):
        return super().accept()
    
    def calculateRank(self):
        if self.internalmarks >= 80:
            print("First Rank")
        elif self.internalmarks >= 60:
            print("Second Rank")
        else:
            print("Third Rank")

# s1 = Student(34256, "Ajay", 25, 80)
# s1.display()

e1=EnggStudent(4256, "Ajay", 25, 80,"Engineering", 61)
e1.accept()
e1.display()




# s1.display()

# s1.calculateRank()
# e1.calculateRank()

        
