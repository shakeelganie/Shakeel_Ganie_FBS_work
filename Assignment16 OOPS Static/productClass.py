'''Create a class Product with members as pid,pname,price and quantity .Add
following methods:
e. Constructor (Support both parameterized and parameterless)
f. Destructor
g. ShowProduct
h. Add static member discount.
i. Provide methods for applying discount on price of product.'''

class Product:
    discount = 0  # static member
    
    def __init__(self, pid=None, pname=None, price=0.0, quantity=None):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        
    def __del__(self):
        print(f"Product object id {self.pid} has been destroyed")

    def showProduct(self):
        print("\nProduct Details")
        print(f"Product Id: {self.pid}")
        print(f"Product Name: {self.pname}")
        print(f"Product Price: {self.price}")
        print(f"Product Quantity: {self.quantity}")

    def discount_price(self):
        total = self.price - (self.price * Product.discount / 100)
        print(f"Price of {self.pname} after {Product.discount}% discount = {total}")
        return total

    @staticmethod
    def discount_value(value):
        Product.discount = value
        print(f"\nDiscount set to {Product.discount}% for all products")


# ---------- Example Usage ----------
p1 = Product(1234, "Table", 200, 4)
p2 = Product(1564, "Chair", 300, 4)
p3 = Product()

p1.showProduct()
p1.discount_price()

p2.showProduct()
p2.discount_price()

# Apply discount
Product.discount_value(5)

# Show discounted prices
p1.discount_price()
p2.discount_price()
p3.discount_price()

        
        