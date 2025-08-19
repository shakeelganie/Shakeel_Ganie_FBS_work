'''Develop a memoization decorator that caches the results of function
calls and returns the cached result when the same inputs occur again.
This can greatly improve the performance of recursive or
computationally intensive functions.'''

# Memoization decorator
def memoize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)  # Store result in cache
        return cache[key]

    return wrapper


# Example usage: Fibonacci (recursive, normally very slow)
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Test
print(fibonacci(40))  # Without memoization this would be super slow!
