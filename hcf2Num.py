# HCF/GCD of two numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


def hcf(num1, num2):

    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i
    return hcf


print("HCF of {0} and {1} is {2}".format(num1, num2, hcf(num1, num2)))

