# 2 Dimension arrays
# Example 1:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)

# Example 2:
print("\nList of numbers: ")
numbers = [5, 2, 1, 2, 7, 4]
print(numbers)
numbers.append(20)
print(numbers)
numbers.insert(0, 10)
print(numbers)
numbers.remove(5)
print(numbers)
numbers.pop()
print(numbers)
print(numbers.index(2))
print(13 in numbers)
print(numbers.count(2))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
numbers.append(13)
print(numbers2)
print(numbers)
numbers.clear()
print(numbers)

# Example 3: (Remove duplicates)
duplicates = [5, 3, 2, 5, 6, 3, 5, 7, 3, 5, 2, 3]
uniques = []
for number in duplicates:
    if number not in uniques:
        uniques.append(number)
print(duplicates)
print(uniques)