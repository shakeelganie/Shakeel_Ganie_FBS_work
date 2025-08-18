''' A list contains the denominations as follows :
D = [2000, 500, 200, 100 , 50, 20, 10, 5]
Accept an amount from user and calculate how many
minimum number of notes will be needed for that
amount.'''


D = [2000, 500, 200, 100, 50, 20, 10, 5]


amount = int(input("Enter the amount: "))

notes_count = {}

for note in D:
    if amount >= note:   
        count = amount // note   
        notes_count[note] = count
        amount = amount % note   


print("\nMinimum number of notes:")
for note, count in notes_count.items():
    print(f"{note} : {count}")


