# Classes

# Example 1:
class Point:
    def move(self):
        print("Moving...")

    def draw(self):
        print("Drawing...")


point1 = Point()
# It's possible to define attributes that are not defined in the class:
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)