# Simple Calculator

num1 = float(input("Enter first number: "))

num2 = float(input("Enter second number: "))


print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Square Root")
print("7. Exit")


choice = int(input("Enter your choice: "))

if choice == 1:
    print(num1, "+", num2, "=", num1 + num2)
elif choice == 2:
    print(num1, "-", num2, "=", num1 - num2)
elif choice == 3:
    print(num1, "*", num2, "=", num1 * num2)
elif choice == 4:
    print(num1, "/", num2, "=", num1 / num2)
elif choice == 5:
    print(num1, "**", num2, "=", num1 ** num2)
elif choice == 6:
    print("Square root of", num1, "=", num1 ** 0.5)
elif choice == 7:
    exit()
else:
    print("Invalid choice")