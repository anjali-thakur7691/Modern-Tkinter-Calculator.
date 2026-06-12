# import math
# print(math.sqrt(25))
# print(math.pi)/

# import calculator
# print(calculator.add(50, 90))


# import mymodule
# print(mymodule.greet("Anjali"))

# Global Scope
# name = "Anjali"
# def greet():
#     print(name)
# greet()
# print(name)
# local vs global
# name = "Global"
# def show():
#     name = "Local"
#     print(name)
# show()
# print(name)

# global keyword
# name = "Anjali"
# def increase():
#     global name
#     name = name + "thakur"
#     print(name)
# increase()

# Enclosing Scope(Nested Function)

# def outer():
#     msg = "Hello"
#     def inner():
#         print(msg)
#     inner()
# outer()

# nonlocal keyword

# def outer():
#     count = 0
#     def inner():
#         nonlocal count
#         count = count + 1
#         print(count)
#     inner()
# outer()
