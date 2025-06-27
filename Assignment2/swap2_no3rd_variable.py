# swap 2 numbers without using the third variable

num1=int(input("Enter number first: "))
num2=int(input("Enter number second: "))

num1=num1+num2
num2=num1-num2
num1=num1-num2
print("Number 1: ", num1)
print("Number 2: ", num2)


# Another way

num1, num2 = num2, num1
print("Number 1: ",num1, "Number 2: ",num2)