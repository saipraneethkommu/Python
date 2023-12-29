#Factorial of a number

# num = int(input("Enter a number: "))

# fact = 1

# if num < 0:
#     print("Factorial does not exist for negative numbers")
# elif num == 0:
#     print("The factorial of 0 is 1")

# else:
#     for i in range(1, num + 1):
#         fact = fact * i

#     print("The factorial of", num, "is", fact)

# Solution 2 using recursion
    
def recur_factorial(num):
    if num == 0:
        return 1
    else:
        return num * recur_factorial(num - 1)

num = int(input("Enter a number: "))
print("Factorial of", num, "is", recur_factorial(num))