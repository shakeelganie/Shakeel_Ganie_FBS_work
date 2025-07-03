# Write a program to prompt user to enter userid and password. 
# After verifying userid and password display a 4 digit random number and ask user to enter the same.
# If user enters the same number then show him success message 
# otherwise failed. (Something like captcha)
import random
user_id=input("Enter your user id: ")
paswd= input("Enter your password: ")

if user_id=="bfs" and paswd=="1234":
    captcha=random.randint(1000, 9999)
    print("Captcha: ",captcha)
    user=int(input("Enter captcha: "))
    if user==captcha:
        print("Login successful")
    else:
        print("Invalid captcha")
else:
    print("Invalid credentials")
