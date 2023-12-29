# Print Fibonacci sequence up to number
# Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

a = 0
b = 1

n = int(input("Enter number: "))

if n == 0:
    print(a)
elif n == 1:
    print(b)
else:
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        print(c)
        a = b
        b = c
