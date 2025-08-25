'''Create a class Distance with data members as km,m and cm and add following
methods :
a. Constructor
b. Destructor
c. Overload +,- operator'''


class Distance:
    def __init__(self, km=0, m=0, cm=0):
        """Constructor"""
        # Normalize values (e.g., 100 cm = 1 m, 1000 m = 1 km)
        total_cm = km * 100000 + m * 100 + cm
        self.km = total_cm // 100000
        rem_cm = total_cm % 100000
        self.m = rem_cm // 100
        self.cm = rem_cm % 100
        print(f"Distance created: {self}")

    def __del__(self):
        """Destructor"""
        print(f"Distance {self} destroyed")

    def __add__(self, other):
        """Overload + operator"""
        if isinstance(other, Distance):
            return Distance(self.km + other.km, self.m + other.m, self.cm + other.cm)
        else:
            raise TypeError("Operand must be of type Distance")

    def __sub__(self, other):
        """Overload - operator"""
        if isinstance(other, Distance):
            total_cm1 = self.km * 100000 + self.m * 100 + self.cm
            total_cm2 = other.km * 100000 + other.m * 100 + other.cm
            if total_cm1 < total_cm2:
                raise ValueError("Resulting distance cannot be negative!")
            diff_cm = total_cm1 - total_cm2
            return Distance(0, 0, diff_cm)  # normalization happens in constructor
        else:
            raise TypeError("Operand must be of type Distance")

    def __str__(self):
        """String representation"""
        return f"{self.km} km {self.m} m {self.cm} cm"
