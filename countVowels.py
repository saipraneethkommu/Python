# Count the Number of Each Vowel

# a = "Harry Potter and the Chamber of Secrets"

# vowels = "aeiou"

# a = a.casefold()

# print(a)

# count = {}.fromkeys(vowels, 0)

# for char in a:
#     if char in count:
#         count[char] += 1

# print(count)

# Solution 2

a = "Harry Potter and the Chamber of Secrets"

vowels = "aeiou"

a = a.casefold()

print(a)

count = {key:sum(1 for char in a if char == key) for key in vowels}

print(count)