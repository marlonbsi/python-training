# Time: 2:14:00
# Tuples: (a list that cannot be modified)

numbers = (1, 2, 3)
# numbers[0] = 10
print(numbers[0])

# Unpacking: (works for tuples and lists)

#Example 1:
coordinates_tuple = (1, 2, 3)
print(coordinates_tuple[0] * coordinates_tuple[1] * coordinates_tuple[2])
x, y, z = coordinates_tuple
print(x, y, z)
# Example 2:
coordinates_list = (4, 5, 6)
a, b, c = coordinates_list
print(f"{a}, {b}, {c} \n")

# Dictionaries:

# Example 3:
customer = {
    "name": "John",
    "age": 30,
    "is_verified": True
}
print(f"Customer name: {customer['name']}")
customer["name"] = "Jack"
print(f"Customer name: {customer.get('name')}")
print(customer.get("birth", "Jan 1 1980"))
customer["birth"] = "Jan 2 1983"
print(customer.get("birth", "Jan 1 1980"))

# Example 4:
numbers = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
}
phone = input("\nPhone number: ")
output = ""
for number in phone:
    n = int(number)
    output += (numbers.get(n, "!") + " ")
print(f"Phone: {output}")

# Example 5:
emojis = {
    ":)": "😊",
    ";)": "😉",
    ":(": "😢",
    "o:)": "😇"
}
message = input("\n> ")
words = message.split(" ")
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)