def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"Factorials from {start} to {end}:")

for i in range(start, end + 1):
    print(f"{i}! = {factorial(i)}")

