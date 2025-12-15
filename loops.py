# range(a, b, c) => a: begin, b: end, c: increment
for number in range(1, 10, 2):
    print("Attempt", number, (number) * ".")

# Attempting until sending successfully:
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Success")
        break
# for-else: if the loop is completed without a break statement:
else:
    print("Attempted 3 times and failed")

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")
    print("\n")

print(type(range(5)))
# Iterable:
for a in "Python":
    print(a)

print("\n")
for b in [1, 2, 3, 4, 5, 6]:
    print(b)

number = 100
while number > 0:
    print(number)
    number //= 2

while True:
    command = input("> ")
    print("ECHO", command)
    if command.lower() == "quit":
        break

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers!")
