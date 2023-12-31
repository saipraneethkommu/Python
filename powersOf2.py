# Display powers of 2 using anonymous function

nterms = int(input("How many terms? "))

result = list(map(lambda x: 2 ** x, range(nterms+1)))

print(result)

# Display powers of 2 using for loop

for i in range(nterms + 1):
    print("2 raised to power", i, "is", result[i])
