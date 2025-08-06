# Python Program to Detect if Two Strings are Anagrams

string1 = input("Enter string1: ")
string2 = input("Enter string2: ")

# Step 1: Check length
if len(string1) != len(string2):
    print("Not an Anagram")
else:
    is_anagram = True

    for char in string1:
        count1 = 0
        count2 = 0
        # Count char in string1
        for c in string1:
            if c == char:
                count1 += 1
        # Count char in string2
        for c in string2:
            if c == char:
                count2 += 1
        # If counts don't match, not anagram
        if count1 != count2:
            is_anagram = False
            break

    if is_anagram:
        print("Anagram")
    else:
        print("Not an Anagram")
