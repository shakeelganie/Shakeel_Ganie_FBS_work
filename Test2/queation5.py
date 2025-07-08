# Calculate the total price of 5 articles with GST

price1=int(input("Enter the price of first products: "))
price2=int(input("Enter the price of second products: "))
price3=int(input("Enter the price of third products: "))
price4=int(input("Enter the price of fourth products: "))
price5=int(input("Enter the price of fifth products: "))
total=price1+price2+price3+price4+price5
gst=total*18/100
total_bill=total+gst
print("Total bill: ", total_bill)
