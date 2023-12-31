# Decimal to Binary using Recursion


def decimalToBinary(num):
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end="")


num = int(input("Enter an integer: "))

decimalToBinary(num)