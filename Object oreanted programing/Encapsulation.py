# class Bank:
#     def __init__(self):
#         self.__balance = 1000
# obj = Bank()
# obj.__balance = 900
# print(obj.__dict__)

# Public Members

# class Student:
#     def __init__(self):
#         self.name = "Anjali"
#     def show(self):
#         print(self.name)
# obj = Student()

# print(obj.name)
# obj.show()

# protected member 
# Singal Underscore
#  _name

# class Parent:
#     def __init__(self):
#         self._salary = 3000
# class Child (Parent):
#     def show(self):
#         print(self._salary)
# obj = Child()
# print(obj._salary)
# obj.show()   


# class demo:
#     def __init__(self):
#         self.public = "public"
#         self.protected = "protected"
#         self.private = "private"

# obj = demo()
# print(obj.public)
# print(obj.protected)
# print(obj.private)

#problem without getter and setter

class Student:
    def __init__(self):
        self.__marks = 0
    def set_marks(self,marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print(self.__marks)
        else:
            print("invalid marks")
s =  Student()
s.set_marks(100)
     