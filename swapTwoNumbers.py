#Swap two numbers with using third variable

x = 13
y = 12

print("The value of x before swapping: ", x)
print("The value of y before swapping: ", y)

#using third variable
temp = x
x = y
y = temp

print("The value of x after swapping: ", x)
print("The value of y after swapping: ", y)

#without using third variable
x = x + y
y = x - y
x = x - y

print("The value of x after swapping: ", x)
print("The value of y after swapping: ", y)
