# Try block:

try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print("Invalid value for age!")
except ZeroDivisionError:
    print("Age must be higher than 0!")