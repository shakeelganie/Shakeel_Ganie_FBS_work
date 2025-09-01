# create a package “SY” which has class SYMARKS (Computer Total, MathsTotal, ElectronicsTotal).

class SYMARKS:
    def __init__(self, ComputerTotal, MathsTotal, ElectronicsTotal):
        self.computerTotal=ComputerTotal
        self.mathTotal=MathsTotal
        self.electronicTotal=ElectronicsTotal

    def display_marks(self):
        print("Marks Obtained:")
        print(f"Computer Total: {self.computerTotal}")
        print(f"Maths Total: {self.mathTotal}")
        print(f"Electronics Total: {self.electronicTotal}")

    def total(self):
        return self.computerTotal + self.mathTotal + self.electronicTotal
