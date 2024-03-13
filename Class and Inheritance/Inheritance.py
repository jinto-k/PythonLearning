class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):  # this is how Dog inherits from Mammal in python
    pass  # to avoid being an empty class


class Cat(Mammal):
    def meow(self):
        print("meow")


bruno = Dog()
bruno.walk()

julie = Cat()
julie.walk()
julie.meow()
