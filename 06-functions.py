def greet(first_name, last_name):
    print(f"\nHi there, {first_name} {last_name}")
    print("Welcome aboard")
    return "..."


def get_greeting(name):
    return f"\nHi {name}"


# by is an optional parameter as it has a default value
def increment(number, by=1):
    return number + by


# *numbers => tuples (iterable list)
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


greet("Marlon", "Andre")
greet("Daniela", "Ojeda")
print(greet("Sonia", "Peron"))

message = get_greeting("Dani")
print(message)
file = open("content.txt", "w")
file.write(message)

# print("\n", increment(2, by=1))
print("\n", increment(2, 5))

print(multiply(2, 3, 4, 5))
