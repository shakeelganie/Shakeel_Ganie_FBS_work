'''Implement a generator function that yields palindrome numbers.
Palindromes are numbers that read the same backward as forward
(e.g., 121, 1331). Generate palindromes lazily and infinitely.'''

# Generator to yield palindrome numbers infinitely
def palindrome_numbers():
    n = 0
    while True:
        if str(n) == str(n)[::-1]:   # Check palindrome
            yield n
        n += 1

# Example usage
gen = palindrome_numbers()

# Print first 20 palindromes
for _ in range(20):
    print(next(gen), end=" ")
