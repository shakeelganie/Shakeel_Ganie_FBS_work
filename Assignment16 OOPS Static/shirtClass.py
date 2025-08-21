'''Create a class Shirt with members as sid,sname,type(formal etc), price and
size(small,large etc) .Add following methods:
j. Constructor (Support both parameterized and parameterless)
k. Destructor
l. ShowShirt
m. For each size of shirt price should change by 10%.
(eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
xlarge=1300) Use static concept.'''

class Shirt:
    price_increment = {
    "small": 0,
    "medium": 10,
    "large": 20,
    "xlarge": 30
}


    def __init__(self, sid=None, sname=None, type=None, price=None, size=None):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.price=price
        self.size=size

    def __del__(self):
        print(f"The shirt object id {self.sid} has been destroyed")

    def showShirt(self):
        print("Shirt Details")
        print(f"Shirt Id: {self.sid}")
        print(f"Shirt Name: {self.sname}")
        print(f"Shirt Type: {self.type}")
        print(f"Shirt Price: {self.price}")
        print(f"Shirt Size: {self.size}")
        

    def updated_price(self):
        if self.size=="small":
            print(f"After increment price: {self.price}")
        elif self.size=="medium":
            price=self.price+self.price*0.10
            print(f"After increment price: {price}")
        elif self.size=="large":
            price=self.price+self.price*0.20
            print(f"After increment price: {price}")
        elif self.size=="xlarge":
            price=self.price+self.price*0.30
            print(f"After increment price: {price}")
        else:
            print("Invalid size")
        


    def incre_price():
        print(f"The increment price of the {Shirt.price_increment}")

s1=Shirt(1234, "Tack", "Formal", 1200, "medium")
s2=Shirt(1235, "Sie", "Casual", 1000, "small")
s3=Shirt(1236, "Ondq", "Classic", 900, "large")
s4=Shirt()

s1.showShirt()
s1.updated_price()
s2.showShirt()
s2.updated_price()
s3.showShirt()
s3.updated_price()

Shirt.incre_price()


        
        
