''' Write a program to prompt user to enter userid and password. If Id and
password is incorrect give him chance to re-enter the credentials. Let him try 3
times. After that program to terminate.'''

correct_user_id="bfs_2025"
correct_password= "1234"

attempts=0
max_attempts=3

while attempts<max_attempts:
    user_id=input("Enter your user id: ")
    password=input("Enter your password: ")

    if user_id==correct_user_id and password==correct_password:
        print("Logged in successfully")
        break
    else:
        attempts+=1

        if attempts<max_attempts:
            print("You have used",attempts,"attempts")
        else:
            print("You have exceeded the attempts")




