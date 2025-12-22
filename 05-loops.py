import random

# While:
number = random.randint(1, 9)
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess_count += 1
    guess = int(input("Guess the number: "))
    if guess == number:
        print("You made it!\n")
        break
else:
    print(f"Failed to guess the number! #{number}\n")

# Example 2:
number = 100
while number > 0:
    print(number)
    number //= 2

# Example 3:
print("\nPrompt 1: ")
while True:
    command = input("> ")
    print("ECHO", command)
    if command.lower() == "quit":
        break

# Example 4:
print("\nPrompt 2: ")
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == 'start':
        if not started:
            print("Car started...")
            started = True
        else:
            print("Error: car already started!")
    elif command == 'stop':
        if started:
            print("Car stopped.")
            started = False
        else:
            print("Error: car already stopped!")
    elif command == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == 'quit':
        break
    else:
        print("I don't understand that!")

# For:

# Example 5:
print("\n")
for b in [1, 2, 3, 4, 5, 6]:
    print(b)

# Example 6 (range(a, b, c) => a: begin, b: end, c: increment)
print("\nFor range increment 2:")
for number in range(1, 10, 2):
    print("Attempt", number, (number) * ".")

# Example 7: (arrays)
print("\nFor in array:")
prices = [10, 20, 50]
total = 0
for price in prices:
    print(f"[{prices.index(price)}]: {price}")
    total += price
print(f"Total: {total}")

# Example 8: (nested loop)
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")
    print("\n")
print(type(range(5)))

# Example 9: (nested loop)
print("\nLetter with nested for: ")
numbers = [5, 2, 5, 2, 2]
for number in numbers:
    for a in range(number):
        print('X' * a)

# Example 10: (List of strings)
names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
print(names)
print(names[0])
print(names[1:4])
print(names[2:])
names[0] = "Jon"
print(names)

# Example 11: (Largest number)
numbers = [3, 5, 1, 7, 4, -2, 8]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print(f"\nLargest number: {largest}")