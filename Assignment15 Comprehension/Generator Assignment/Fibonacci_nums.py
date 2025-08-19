'''We want to generate Fibonacci numbers up to a certain limit.
Instead of computing and storing the entire sequence in memory,
create generator to yield Fibonacci numbers one by one,
conserving memory and allowing for easy iteration.'''


# Fibonacci generator
def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

# Take input from user
limit = int(input("Enter the limit: "))

print("Fibonacci numbers up to", limit, ":")
for num in fibonacci(limit):
    print(num, end=" ")
