# class Bike():
#     def fuel_system(self):
#         print("Fuel Injected")
#     def spark(self):
#         print("Spark Generat")
#     def piston(self):
#         print("Piston moving")
# bike = Bike()
# bike. fuel_system()

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
        def sound(self):
            print("Bark")

obj = Dog()
obj.sound()