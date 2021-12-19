from src.utils import map
from src.list_extensions import List

input = List.from_values(1, 2, 3, 4)
square = lambda x: x ** 2

# prints [1, 4, 9, 16]
input.map(square)\
     .to_list()\
     .pipe(print)
