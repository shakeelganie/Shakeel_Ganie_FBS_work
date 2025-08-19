'''Create a class Book with members as bid,bname,price and author.Add following
methods:
a. Constructor (Support both parameterized and parameterless)
b. Destructor
c. ShowBook'''

class Book:
    def __init__(self,bid=None, bname=None,price=0.0, author=None):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author

    def __del__(self):
        print(f"Book object with ID {self.bid} is destroyed.")

    def ShowBook(self):
        print("Book Details")
        print(f"Book ID: {self.bid}")
        print(f"Book Name: {self.bname}")
        print(f"Book Price: {self.price}")
        print(f"Book Author: {self.author}")

book1=Book(1001,"The World",2000,"Tom")
book1.ShowBook()

book2=Book(1002,"End of World",2500,"Hansen")
book2.ShowBook()
