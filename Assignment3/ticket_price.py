# Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

age1=int(input("Enter the age1: "))
age2=int(input("Enter the age2: "))
age3=int(input("Enter the age3: "))
age4=int(input("Enter the age4: "))
age5=int(input("Enter the age5: "))
ticket_price=int(input("Enter the ticket price: "))
total=0

if age1<=12:
    total+=ticket_price-ticket_price*0.30
elif age1>=59:
    total+=ticket_price-ticket_price*0.50
else:
    total+=ticket_price

if age2<=12:
    total+=ticket_price-ticket_price*0.30
elif age2>=59:
    total+=ticket_price-ticket_price*0.50
else:
    total+=ticket_price

if age3<=12:
    total+=ticket_price-ticket_price*0.30
elif age3>=59:
    total+=ticket_price-ticket_price*0.50
else:
    total+=ticket_price

if age4<=12:
    total+=ticket_price-ticket_price*0.30
elif age4>=59:
    total+=ticket_price-ticket_price*0.50
else:
    total+=ticket_price

if age5<=12:
    total+=ticket_price-ticket_price*0.30
elif age5>=59:
    total+=ticket_price-ticket_price*0.50
else:
    total+=ticket_price

print("Total amount of all the five tickets: ", total)