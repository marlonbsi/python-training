def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum


import random
class Dice:
    def roll(self):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        return a, b