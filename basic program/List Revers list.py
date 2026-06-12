# Revers list
# num = [1,2,3,4,8,9,66,44,88]
# i = len(num) - 1
# while i >= 0:
#     print(num[i], end=" ")
#     i = i -1
# MULTIPLY LIST ELEMENTS

# a = [1,2,3]
# i = 0
# result = 1
# while i < len(a):
#     result = result * a[i]
#     i = i + 1
# print(result)
# print only string number
# a = [1, "hello" , 3, "a", "hi"]
# i = 0
# while i < len(a):
#     # if type(a[i]) == str:
#         print(a[i])
#         i = i + 1

a = [5,12,7,20,40]

i = 0

while i < len(a):
    if a[i] < 10:
        print(a[i])
        i = i + 1
