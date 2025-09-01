# Create another package “TY” which has a class TYMarks (Theory, Practical).

# TY/TYMARKS.py

class TYMARKS:
    def __init__(self, theory, practical):
        self.theory = theory
        self.practical = practical

    def display_marks(self):
        print("TY Marks Obtained:")
        print(f"Theory: {self.theory}")
        print(f"Practical: {self.practical}")

    def total(self):
        return self.theory + self.practical


