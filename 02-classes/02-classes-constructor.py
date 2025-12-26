# Classes:

# Example 1: (Point)
class Point:
    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("Moving...")

    def draw(self):
        print("Drawing...")

    def show(self):
        print(f"Point: {self.x}, {self.y}")


point = Point(10, 20)
point.show()

# Example 2: (Person)
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}!")


p1 = Person("Marlon")
p1.talk()

p2 = Person("Bob")
p2.talk()