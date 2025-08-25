'''Create a class Student with following
a. data members :
i. StudentId
ii. Name
iii. Age
iv. Percentage
b. Add the following methods :
i. Parameterized constructor
ii. Display
iii. Accept
iv. Method CalculateRank
v. Override __str__ Method'''

class Student:
    def __init__(self, studentId=1234, name="", age=0, percentage=0.0):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage
        self.rank = None   # store rank later

    def __str__(self):
        return (f"Student Id: {self.studentId}, "
                f"Name: {self.name}, "
                f"Age: {self.age}")
                

    def display(self):
        print(f"Student Details")
        print(f"Student Id: {self.studentId}")
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")
        print(f"Student Percentage: {self.percentage}")
        if self.rank:
            print(f"Student Rank: {self.rank}")

    def accept(self):
        self.studentId = int(input("Enter Student ID: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))

    def calculateRank(self):
        if self.percentage >= 80:
            self.rank = "First Rank"
        elif self.percentage >= 60:
            self.rank = "Second Rank"
        else:
            self.rank = "Third Rank"

 
        


