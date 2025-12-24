# Functions:

# Example 1:
def greet(first_name, last_name):
    print(f"\nHi there, {first_name} {last_name}")
    print("Welcome aboard")
    return "..."


# Example 2:
def get_greeting(name):
    return f"\nHi {name}"


# Example 3:
# by is an optional parameter as it has a default value
def increment(number, by=1):
    return number + by


# Example 4
# *numbers => tuples (iterable list)
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


# Example 5:
def square(number):
    return number * number


# Example 6: (emoji converter)
def emoji_converter(text):
    emojis = {
        ":)": "😊",
        ";)": "😉",
        ":(": "😢",
        "o:)": "😇"
    }
    words = message.split(" ")
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


greet("Marlon", "Andre")
greet(last_name = "Ojeda", first_name = "Daniela")
print(greet("Sonia", "Peron"))

message = get_greeting("Dani")
print(message)
file = open("content.txt", "w")
file.write(message)

# print("\n", increment(2, by=1))
print(f"\n{increment(2, 5)}")

print(f"\n{multiply(2, 3, 4, 5)}")

print(square(int(input("\nCalculate square: "))))

while True:
    print("\nEnter -quit- to exit:")
    message = input("> ")
    if message == "quit":
        break
    else:
        print(emoji_converter(message))
