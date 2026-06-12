# Class
# car - car ek class hai
# object hai
# properties - car ki khubiya
# color
# brand
# speed
# behaviours- car ke function hai 
# start()
# brake()
# accelerate ()

# counstructor
# __init__()
# class student:
#     def __init__(self, name, age, rollNo):
#         self.name = name
#         self.age = age
#         self.rollNo = rollNo


# s1 = student("Rahul", 25, 566)

# print(s1.name)
# print(s1.age)
# print(s1.rollNo)

# clss
# objects
# self
#  properties (atributes)
# methods (behaviars)

# class
# Dog
# class Dog:
#     def __init__(self):
#         self.name = "monti"
#     def bark(self):
#         print("bark")
#     def eat(self):
#         print("eating")

# dog1 = Dog()

# dog1.bark()
# dog1.eat()
# print(dog1.name)

# Types of Inheritance
# 1- Singal inheritance? - Ek child class sirf ek hi parent class se inherit karti hai

# class child(parent):
# pass
# class Animal():
#     def eat(self):
#         print("Animal. can eat")
# class Dog(Animal):
#     def bark(self):
#         print("Dog Barks")
# ani = Animal()
# ani.eat()
# # ani.bark()

# d = Dog()
# d.bark()
# d.eat()
#                    2 Example
# class father():
#     def bike(self):
#         print("father has bike")
# class son(father):
#     def mobile(self):
#         print("son has mobile")

# s1 = son()
# s1.mobile()
# s1.bike()
        
# 2. Multiple Inheritance? - Ek Child hota hai or multipal Parent hote hai

# class Father:
#     def money(self):
#         print("father gives money")
# class Mother:
#     def care(self):
#         print("mother gives care")
# class Child(Father, Mother):
#     def fun(self):
#         print("child enjoying")
# c = Child() Object

# c.money()
# c.care()
# c.fun()
# 3. Multilevel inheritance? - inharitance chain me hoti hai (Grandfather- Parent- child)

# class Grandfather:
#     def property(self):
#         print("Wones property")
# class Father(Grandfather):
#     def car(self):
#         print("father has care")
# class son(Father):
#     def laptop(self):
#         print("son has laptop")
# s = son()
# s.laptop()
# s.car()
# s.property()

# 4- Hierarchical Inheritance - Ek Parent Class se multiple child classes inherit karti hai

# class Animal:
#     def eat(self):
#         print("animal eats")

# class Dog(Animal):
#     def bark(self):
#         print("dog barks")
# class Cat(Animal):
#     def meow(self):
#         print("cat meows")
# C = Cat()
# C.eat()
# C.meow()
# 5- Hybrid Inheritance- Different inheritance ka combination hota hai

class A:
    def showA(self):
        print("A")
class B(A):
    def showB(self):
        print("B")
class C(A):
    def showC(self):
        print("C")
class D(B,C):
    def showD(self):
        print("D")

obj = D()

obj.showC()
obj.showD()