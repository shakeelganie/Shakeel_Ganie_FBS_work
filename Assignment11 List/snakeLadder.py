# Print 1 to 100 in snakes and ladder pattern.

main=[]
lst=[]
row=1

for i in range(1,101):
    lst.append(i)
    if i%10==0:
        if row%2==0:
            lst.reverse()
        main.append(lst)
        row+=1
        lst=[]
main.reverse()
print(main)

        
