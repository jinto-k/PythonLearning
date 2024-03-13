class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()  # note that we don't use new keyword create an instance
point1.draw()

point1.x = 10
print(point1.x)


class Person:

    # init is the constructor
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f" Hi I am {self.name}")


John = Person("John")
Bob = Person("Bob")
John.talk()
Bob.talk()
