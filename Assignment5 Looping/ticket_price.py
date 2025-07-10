'''Accept no. of passengers from user and per ticket cost. Then accept age of each
passenger and then calculate total amount to ticket to travel for all of them based on
following condition :
a. Children below 12 = 30% discount
b. Senior citizen (above 59) =50% discount'''


total = 0
n = int(input("Enter the number of passengers: "))
tp = float(input("Enter the per ticket cost: "))

for i in range(1, n + 1):
    age = int(input(f"Enter the age of passenger {i}: "))
    
    if age < 12:
        cost = tp * 0.70  # 30% discount
    elif age > 59:
        cost = tp * 0.50  # 50% discount
    else:
        cost = tp         # no discount

    print(f"Ticket cost for passenger {i}: {cost}")
    total += cost

print("Total price of all the tickets is:", total)
