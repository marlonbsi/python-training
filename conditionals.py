# simple concditional:
temperature = 15
if temperature > 30:
    print("it's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")

# ternary operator:
age = 12
message = "Eligible to university" if age >= 18 else "Not Eligible to university"
print(message)

# logical operators: and, or, not:
high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible for bank loan")
else:
    print("Not eligible for bank loan")

if high_income and good_credit or student:
    print("Eligible for government loan")

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
