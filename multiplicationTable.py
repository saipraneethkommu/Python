# Display Multiplication Table

# using while loop
    
n = int(input("Enter a number: "))

i = 1

while i <= 10:
    print("{} x {} = {}".format(n, i, n * i))
    i += 1

# using for loop
    
n = int(input("Enter a number: "))

for i in range(1, 11):
    print("{} x {} = {}".format(n, i, n * i))