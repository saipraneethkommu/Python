# prime numbers for given interval

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

for num in range(start, end + 1):

    # all prime numbers are greater than 1
    if num > 1:
         for i in range(2, num):
              if (num % i) == 0:
                    break
         else:
              print(num)
    
