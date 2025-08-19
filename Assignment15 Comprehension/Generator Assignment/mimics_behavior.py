'''Write a generator function that mimics the behavior of the built-in
range() function. The generator should take start, stop, and step
arguments and yield numbers within the specified range.'''

# Custom range generator
def my_range(start, stop=None, step=1):
    if stop is None:   # Handle case when only one argument is given
        stop = start
        start = 0

    if step == 0:
        raise ValueError("step argument must not be zero")

    if step > 0:
        while start < stop:
            yield start
            start += step
    else:  # step < 0
        while start > stop:
            yield start
            start += step


# Example usage
print("my_range(5):")
for num in my_range(5):
    print(num, end=" ")

print("\n\nmy_range(2, 10, 2):")
for num in my_range(2, 10, 2):
    print(num, end=" ")

print("\n\nmy_range(10, 2, -2):")
for num in my_range(10, 2, -2):
    print(num, end=" ")
