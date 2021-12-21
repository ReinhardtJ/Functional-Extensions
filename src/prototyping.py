from src.functional_extensions import List

input = List.from_values(1.5, 1.5)
square = lambda x: x ** 2

# prints [1, 4, 9, 16]
output = input.enumerate()
print(1.5 in output)