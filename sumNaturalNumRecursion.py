# Sum of Natural Numbers using Recursion

num = int(input("Enter a number: "))


def sumOfNaturalNumbers(num):

    if num == 0:
        return 0
    else:
        return num + sumOfNaturalNumbers(num - 1)
    

print("The sum of natural numbers from 1 to", num, "is", sumOfNaturalNumbers(num))