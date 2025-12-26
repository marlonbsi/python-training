#Variables, input, output

#Example 1:
full_name = "Marlon Andre"
age = 42
is_new = True

#Example 2:
name = input("What is your name? ")
favorite_color = input("What is your favorite color? ")
print(name + ' likes ' + favorite_color)

#Example 3:
birth_year = input("Birth year? ")
print(type(birth_year))
age = 2025 - int(birth_year)
print(type(age))
print(age)

#Example 4:
weight_lbs = input("Weight (lbs)? ")
weight_kgs = int(weight_lbs) * 0.45
print(weight_kgs)

#Example 5:
name = 'Jennifer'
print(name[1:-1])

#Example 6:
first = 'Marlon'
last = 'Generoso'
message = first + ' [' + last + '] ' + 'is a coder'
print(message)