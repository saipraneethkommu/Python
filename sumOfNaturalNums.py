# Sum of Natural Numbers

num = int(input("Enter a number: "))

sum = 0

# find the sum of numbers from 1 to num
for i in range(1, num + 1):
    sum += i

print("The sum of natural numbers from 1 to", num, "is", sum)

# using whiile loop

num = int(input("Enter a number: "))

sum = 0

i = 1

while i <= num:
    sum += i
    i += 1

print("The sum of natural numbers from 1 to", num, "is", sum)