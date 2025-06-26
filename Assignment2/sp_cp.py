# calculate selling price of a book based on cost price and discount

cp=int(input("Enter the cost price of the book: "))
discount=int(input("Enter the discount percentage: "))

discount_amount=cp*discount/100
sp=cp-discount_amount
print("The selling price of the book is: ",sp)