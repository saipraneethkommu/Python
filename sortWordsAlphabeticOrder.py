a = "Harry Potter and the Chamber of Secrets"

b = a.split()

print(b)

for i in range(len(b)):
    b[i] = b[i].lower()

print(b)

b.sort()

print(b)
