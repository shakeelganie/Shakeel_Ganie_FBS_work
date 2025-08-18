'''There is a list with some numbers. Create a new
dictionary using this list in such a way that key is
number and value is frequency of occurrence of that
number in list.

[1,3,4,1,2,3,6,7,1,2,4]
{1:3,3:2,2:2,'''

nums = [1, 3, 4, 1, 2, 3, 6, 7, 1, 2, 4]

freq = {}  # empty dictionary

for n in nums:
    freq[n] = freq.get(n, 0) + 1   # count frequency

print(freq)
