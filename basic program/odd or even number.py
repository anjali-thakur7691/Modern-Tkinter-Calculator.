#n = 15

#if n % 2 == 0:
 #   print(n, " is an even number")
#else:
 #   print(n, " is an odd nmber")


# numbers = [15,22,37,40,9]

# for n in numbers:
#     if n % 2 == 0:
#         print(n, " is an even number")
# else:
#         print(n, " is an odd nmber")


# number = "458"
# even = 0
# odd = 0
# for digit in number:
#     d = int(digit)
#     if d % 2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1
# print("total even digits:",even)
# print("total odd digits",odd)

# Find the largest digit of a number

# number = 58964327
# largest = max(str(number))
# print("sabes bada digit hai:",largest)

# number = "1020304050"
# largest = 0
# for digit in number:
#     d = int(digit)
#     if d > largest:

#          largest = d
# print("Largest digit is",largest)/

# Find the smallest number

number = "1234"
smallest = 0
for digit in number:
    d = int(digit)
    if d > smallest:
        smallest = d
print ("smallest digit is",smallest)
