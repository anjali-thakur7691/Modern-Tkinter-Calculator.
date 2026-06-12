# class Animal:
#     def sound(self):
#         print("Animal Sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog bark")

# dog = Dog()
# dog.sound()

# Method 2 - *args
# class calculator:
#     def add (self,a,b,c,d):
#         return a + b + c + d
# c = calculator()
# print(c.add(2,3,3,1))


# class calculator:
#     def add (self, *args):
#         return sum(args)
# c = calculator()
# print(c.add(2,8))

# method 3 : **Kwargs
class person:
    def info(self, **kwargs):
        print(kwargs)
p = person()
p.info(name="Anjali", age= 25, )
