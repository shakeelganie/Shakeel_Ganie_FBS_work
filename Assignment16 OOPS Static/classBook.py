'''1. Create a class Book with members as bid,bname,price and author.Add following
methods:
a. Constructor (Support both parameterized and parameterless)
b. Destructor
c. ShowBook
d. Add static variable count and also maintain count of objects created.'''

class Book:
    count=0
    def __init__(self, bid=None, bname="", price=0.0, author=""):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author
        Book.count+=1


    def __del__(self):
        print(f"Book object with Id: {self.bid} has been destroyed")


    def ShowBook(self):
        print("Book Details")
        print(f"Bood Id: {self.bid}")
        print(f"Book name: {self.bname}")
        print(f"Book price: {self.price}")
        print(f"Book author: {self.author}")
        
    @staticmethod
    def get_count():
        print(f"Total books created {Book.count}")

book1=Book(1234, "The man", 1200, "hansen")
book2=Book(1234, "The man", 1200, "hansen")
book3=Book()    #parameterless

book1.ShowBook()
print()
book2.ShowBook()
print()
book3.ShowBook()
print()

Book.get_count()   

    
    