from SY import SYMARKS
from TY import TYMARKS
from SY_TY import Student

def main():
    # Create SY and TY marks objects
    sy = SYMARKS(ComputerTotal=35, MathsTotal=80, ElectronicsTotal=72)
    ty = TYMARKS(theory=40, practical=85)

    # Create Student object
    student1 = Student(roll_no=101, name="Shakeel", sy_marks=sy, ty_marks=ty)

    # Display result
    student1.display_result()

if __name__ == "__main__":
    main()
