import random

# Example 1:
for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10, 20))

# Example 2:
members = ['John', 'Mary', 'Bob', 'Mosh']
for i in range(3):
    leader = random.choice(members)
    print(leader)

# Example 3:
from utils import Dice

dice = Dice()
for i in range(3):
    print(dice.roll())