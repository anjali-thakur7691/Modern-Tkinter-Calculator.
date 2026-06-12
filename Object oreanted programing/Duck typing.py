
class Duck:
    def speak (self):
        print("Quack")
class Human:
    def speak(self):
        print("Hello")
def make_sound(obj):
    obj.speak()
make_sound(Duck())
make_sound(Human())