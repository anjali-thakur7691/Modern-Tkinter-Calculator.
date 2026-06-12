# #DEF ()FUNCTION
# def calc2():
#     a = int(input("enter a:"))
#     b = int(input("enter b:"))
#     op = input("enter operator:")
#     match op:
#         case "+":
#             print(a+b)
#         case "-":
#             print(a-b)
#         case "**":
#             print(a*b)
#         case "//":
#             print(a/b)
#         case _:
#             print("invalid op")


def my_count(lst, value):
     count = 0
     for item in lst:
          if item == value:
               count = count + 1
     return count
num = [1,2,3,4,5,2]
print(my_count(num,3))

