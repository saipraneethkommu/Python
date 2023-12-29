#Solution 1 (Using Exponentiation)

# num = 64
num = int(input("Enter a number: "))

sr = num ** 0.5

print("Square root of", num, "is", sr)

#Solution 2 (Using Math Module)

import math

num2 = int(input("Enter a number: "))

sr2 = math.sqrt(num2)

print("Square root of", num2, "is", sr2)