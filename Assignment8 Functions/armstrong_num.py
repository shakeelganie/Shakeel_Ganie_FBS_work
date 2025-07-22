# WAP to check if a given number is Armstrong number or not.

def check_armstrong_number():
    # take input from the user
    num = int(input("Enter a number: "))

    # initialize sum
    total = 0

    # find the sum of the cube of each digit
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10

    # display the result
    if num == total:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")

# call the function
check_armstrong_number()


