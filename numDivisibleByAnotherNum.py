# Number divisible by Another Number

# num = int(input("Enter a number: "))

# for i in range(1, 101):
#     if i % num == 0:
#         print(i)

# Solution 2 using lambda function and filter

l = [39, 48, 26,13,36,16,173,243,13]

result = list(filter(lambda x: (x % 13 == 0), l))

print("Numbers divisible by 13 are", result)