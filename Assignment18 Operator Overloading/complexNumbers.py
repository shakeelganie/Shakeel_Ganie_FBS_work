'''Create a class Complex Number with data members as real and imag and add
following methods :
a. Constructor
b. Destructor
c. Overload +,- operator'''

class ComplexNumber:
    def __init__(self, real=0.0, imag=0.0):
        """Constructor"""
        self.real = real
        self.imag = imag
        print(f"ComplexNumber created: {self}")

    def __del__(self):
        """Destructor"""
        print(f"ComplexNumber {self} destroyed")

    def __add__(self, other):
        """Overload + operator"""
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        else:
            raise TypeError("Operand must be of type ComplexNumber")

    def __sub__(self, other):
        """Overload - operator"""
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imag - other.imag)
        else:
            raise TypeError("Operand must be of type ComplexNumber")

    def __str__(self):
        """String representation"""
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"
