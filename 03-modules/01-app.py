# Modules:

# Example 1:
# import whole module:
import converters

print(converters.kg_to_lbs(72))
print(converters.lbs_to_kg(160))

# Example 2:
# import part of the module:
from converters import kg_to_lbs

print(kg_to_lbs(72))

# Example 3:
from utils import find_max
numbers = [9, 5, 3, 7, 9, 2, 11, 4]
print(find_max(numbers))

# Same with built-in max function:
print(max(numbers))