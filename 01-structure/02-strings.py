#Example 1:
print("Hello World 😁")
print("*" * 50, "\n" + "*" * 40, "\n" + "*" * 30)

students_count = 1000
rating = 4.99
is_published = False
course = "Python Programming"
escape_char = "Testing \nEscape"
# \"
# \\
# \'
# \n

#Concatenation:
first_name = "Marlon"
last_name = "Andre"
full_name = f"{len(first_name)} {last_name}"
# We can use any valid expressions inside {}
msg = first_name + ' [' + last_name + ']' + ' is a coder.'
print(full_name)
print(msg)

#String array:
print(students_count, ", ", rating, ", ", is_published, ", ", course)
print(len(course))
print(course[0])
print(course[-1])
print(course[4:])
print(course[:4])
print(escape_char)

#String methods:
course_capital = course.upper()
print(course_capital)
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("Pro"))
print(course.replace("P", "J"))
print("Pro" in course)
print("gram" not in course)
