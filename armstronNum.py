# check Armstrong number

num = int(input("Enter a number: "))
order = len(str(num))

sum = 0

temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")



# check Armstrong number in an interval

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

for num in range(start, end + 1):

    # order of number
    order = len(str(num))
    
    # initialize sum
    sum = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
        
    if num == sum:
        print(num)



