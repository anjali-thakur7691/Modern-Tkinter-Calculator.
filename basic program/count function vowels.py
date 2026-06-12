
#  a = "hello"

#  i = 0
#  count = 0

# while i < len(a):
#     if a[i] in "aeiou":
#          count = count + 1
#     i = i + 1

# print("vowels :",count)

# count uppercase letters
# a = "HelloWorld"
# i = 0
# count = 0

# while i < len(a):
#     if a[i].isupper():
#         count = count + 1
#     i = i + 1
# print(count)

# COUNT NEGATIVE NUMBERS IN LIST

# a = [1,-2,-3,-4,4,5]
# i = 0
# count = 0
# while i < len(a):
#     if a[i] < 0:
#         count = count + 1
#         print(a[i])
#     i = i + 1
# print("negative numbers:",count)
# count spaces in string
# a = " hello bhai kaise ho ? "
# i = 0
# count = 0
# while i < len(a):
#     if a[i] == " ":
#         count = count + 1
#     i = i + 1

# print(count)
# COUNT CONSONANTS

a = "hello"
i = 0
while i < len(a):
    if a[i] not in "aeiou":
        count = count + 1
    i = i +1
print(count)



