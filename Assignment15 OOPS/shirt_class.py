'''Create a class Shirt with members as sid,sname,type(formal etc), price and
size(small,large etc) .Add following methods:
g. Constructor (Support both parameterized and parameterless)
h. Destructor
i. ShowShirt'''

class Shirt:
    def __init__(self, sid=None, sname=None, type=None, price=0.0, size=None):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.price=price
        self.size=size

    def __del__(self):
        print(f"Shirt object with ID {self.sid} is destroyed.")

    def ShowShirt(self):
        print("Shirt Details")
        print(f"Shirt ID: {self.sid}")
        print(f"Shirt Name: {self.sname}")
        print(f"Shirt Type: {self.type}")
        print(f"Shirt Price: {self.price}")
        print(f"Size: {self.size}")

shirt1=Shirt(1001,"Denim shirt","Formal",1200,"Large")
shirt1.ShowShirt()

shirt2=Shirt(1002,"Flannel shirt","Casual",1000,"Small")
shirt2.ShowShirt()