#  Write a program to find sum of digits of a number.


def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10      # Get the last digit
        total += digit        # Add it to total
        num = num // 10       # Remove the last digit
    return total

num = int(input("Enter a number: "))
result=sum_of_digits(num)
print("Sum of digits:", result)
