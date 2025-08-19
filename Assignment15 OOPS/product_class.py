'''Create a class Product with members as pid,pname,price and quantity .Add
following methods:
d. Constructor (Support both parameterized and parameterless)
e. Destructor
f. ShowProduct'''

class Product:
    def __init__(self,pid=None, pname=None,price=0.0, quantity=None):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantity

    def __del__(self):
        print(f"Product object with ID {self.pid} is destroyed.")

    def ShowProduct(self):
        print("Product Details")
        print(f"Product ID: {self.pid}")
        print(f"Product Name: {self.pname}")
        print(f"Product Price: {self.price}")
        print(f"Quantity: {self.quantity}")

product1=Product(1001,"Washing Machine",16000,3)
product1.ShowProduct()

product2=Product(1002,"Refrigerator",20000,2)
product2.ShowProduct()