from pathlib import Path

# Absolute path:
#  -> Windows: c:\d1\d2\file.txt
#  -> Linux/Mac: /usr/local/bin
#  Relative path:
#  -> path navigating from the current directory.

# Example 1:
path = Path("ecommerce")
print(path.exists())
print(path.absolute())

path = Path("emails")
path.mkdir()
path = Path("emails")
path.rmdir()

# Example 2:
path = Path()
for file in path.glob('*.py'):
    print(file)