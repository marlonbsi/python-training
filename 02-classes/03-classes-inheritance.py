# Classes - Inheritance

# Example 1:
class Mammal:
    def walk(self):
        print("Walking...")

class Dog(Mammal):
    def bark(self):
        print("Au au")


class Cat(Mammal):
    def be_the_boss(self):
        print("Being the boss...")


dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.be_the_boss()