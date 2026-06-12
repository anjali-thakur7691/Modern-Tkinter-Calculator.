# itterable
#iter
# decorators
# generators
# itarator
# next
# yeild
# nums = [1,2,3,4,5,6]
# x = iter(nums)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# name = "Anjali"
# x = iter(name)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# num = [1,2,3,4,5,6]
# def count():
#     for i in range(5):
#         yield i
# for num in count():
#     print(num)

# Decorator()
# Decorator ek function hai jo use kiya jata hai dusre function ko modify krne ke liye but bina original cod me change kiye
# def my_decorator(func):
#     def wrapper():
#       print("Before function")
#       func()
#       print("After function")
#     return wrapper
    
# @my_decorator
# def hello():
#       print("Hello Bhai")

# hello()
def gift():
    print("watch")
def wrapper(func):
    def inner():
        print("gift wrapper start")
        func()
        print("Ribbon added")
    return inner
gift = wrapper(gift)
gift()