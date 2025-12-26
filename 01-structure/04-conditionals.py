# Pure boolean:
is_hot = True
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day!")

# Simple conditional:
temperature = 15
if temperature > 30:
    print("\nit's warm")
    print("Drink water")
elif temperature > 20:
    print("\nIt's nice")
else:
    print("\nIt's cold")
print("Done")

# Ternary operator:
age = 12
message = "Eligible to university" if age >= 18 else "Not Eligible to university"
print(message)

# Intervals:
# age should be between 18 and 65
age = 12
# if age >= 18 and age < 65:
if 18 < age < 65:
    print("Age eligible")

if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")

# Example 1:
price = 1000000
good_credit = False
if good_credit:
    price = price * 0.9
else:
    price = price * 0.8
print(f"Final price: ${price:.2f}")

# Example 2: (logical operators: and, or, not)
high_income = False
good_credit = True
student = False
if (high_income or good_credit) and not student:
    print("Eligible for bank loan")
else:
    print("Not eligible for bank loan")

if high_income and good_credit or student:
    print("Eligible for government loan")
else:
    print("Not eligible for government loan")

# Example 3:
name = 'J'
if len(name) < 3:
    print("\nName must be at least 3 characters")
elif len(name) > 20:
    print("\nName must be a maximum of 20 characters")
else:
    print("\nName looks good!")

# Example 4:
weight = int(input("\nWeight: "))
unit = input("(L)bs or (K)g: ").upper()
if unit == "L":
    weight = weight * 0.45
    print(f"You weight in Kgs: {weight:.2f}")
else:
    weight = weight / 0.45
    print(f"You weight in Lbs: {weight:.2f}")
