# Factorial of Number using Recursion

num = int(input("Enter a number: "))

def Factorial(num):
    if num == 0:
        return 1
    else:
        return num * Factorial(num-1)

print("Factorial of", num, "is", Factorial(num))