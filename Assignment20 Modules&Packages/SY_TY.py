'''Create object of student class (Outside SY & TY package) having roll
number, name, SYMakrs and TYMarks. Add the marksof SY and TY
Computer subjects and calculate grade ("A" for >=70, "B" for >=60,
"C" for >=50, “Pass Class” for >=40 else “Fail”) and display the result
of the student in proper format.'''

from SY import SYMARKS
from TY import TYMARKS

class Student:
    def __init__(self, roll_no, name, sy_marks: SYMARKS, ty_marks: TYMARKS):
        self.roll_no = roll_no
        self.name = name
        self.sy_marks = sy_marks
        self.ty_marks = ty_marks

    def calculate_computer_total(self):
        # Adding Computer Total from SY and Theory from TY
        return self.sy_marks.computerTotal + self.ty_marks.theory

    def calculate_grade(self):
        total = self.calculate_computer_total()
        if total >= 70:
            return "A"
        elif total >= 60:
            return "B"
        elif total >= 50:
            return "C"
        elif total >= 40:
            return "Pass Class"
        else:
            return "Fail"

    def display_result(self):
        print("=" * 40)
        print(f"Roll No   : {self.roll_no}")
        print(f"Name      : {self.name}")
        print(f"SY Computer Marks : {self.sy_marks.computerTotal}")
        print(f"TY Theory Marks   : {self.ty_marks.theory}")
        print(f"Computer Total    : {self.calculate_computer_total()}")
        print(f"Grade             : {self.calculate_grade()}")
        print("=" * 40)
