#object creation me 2 methods call hoti hai
# __init__()
# __new__()
# new ()- object ko memory allocate , object create
# init()- objectqinitize karta hai

# class Student:
#     def __new__(cls):
#         print("object created")
#         return super().__new__(cls)
#     def __init__(self):
#         print("object initilized")

#     def greet(self):
#         print("hello")
# s = Student()
# s.greet()

# class Student:
#     pass
# s1 = Student()
# print(type(Student))

# class Student:
#     def __str__(self):
#         return "Student object"
# s = Student()
# print(s)

# class Student:
#     def __init__(self,name):
#         self.name = name
#     # def __str__(self):
#     #     return f"Student Name. {sekf.naem}"
# s = Student("Anjali")
# print(s)

class Student:
    def __repr__(self):
        
        return "Student(Anjali)"
s = Student()
print(repr(s))