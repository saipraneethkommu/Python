# Largest among 3 numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print("The largest number is", largest)

# smallest among 3 numbers

if(num1 <= num2) and (num1 <= num3):
    smallest = num1
elif(num2 <= num1) and (num2 <= num3):
    smallest = num2
else:
    smallest = num3

print("The smallest number is", smallest)