import math

x = 1
x = 1.1
x = 1 + 2j  # a + bi

print(10 - 3)
print(10 + 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)  # int division
print(10 % 3)
print(10 ** 3)  # power, exponentiation

# Precedence :
# 1. Parenthesis
# 2. Exponentiation
# 3. Multiplication or division
# 4. Addition or subtraction.

x = 10
x = x + 3
x += 3
print(x)

x = (10 + 3) * 2 ** 2
print(f"X: {x}")

print(round(2.9))
print(abs(-2.9))

print(math.ceil(2.2))
print(math.factorial(5))
print(math.trunc(3.4))
print(math.isinf(x))

x = input("x: ")
print(type(x))
y = int(x) + 1
print(f"x: {x}, y: {y}")

# Falsy:
# ""
# 0
# None
print(bool(0))
print(bool(1))
print(bool(5))
print(bool(False))
print(bool(-2))
