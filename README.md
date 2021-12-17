# List-Extensions

Use lists in Python by calling functions on them. Why? Because every function
returns a new instance of a list, which not only prevents mutating the original
list but also makes it possible to chain functions and build a coherent and
readable series of operations.

## Usage
```python
# initialize an extended list by either passing a regular list to __init__ or 
# calling the from_values function

from src.list_extensions import List

regular_list = [1, 2, 3, 4]
extended_list_1 = List([1, 2, 3, 4])
extended_list_2 = List.from_values(1, 2, 3, 4)
assert regular_list == extended_list_1 == extended_list_2
```
## Available functions
### map
```python
from src.list_extensions import List

input = List.from_values(3, 6, 1, 2, 9)

# instead of
map(lambda x: x ** 2, input)
# or
[x ** 2 for x in input]
# write
input.map(lambda x: x**2)
```
### for_each
```python
from src.list_extensions import List

input = List.from_values(3, 6, 1, 2, 9)

# instead of
for i in input:
    print(i)
#write
input.for_each(print)
```
### sort
```python
from src.list_extensions import List

input = List.from_values(3, 6, 1, 2, 9)

# instead of
sorted = input.copy().sort()
# write
sorted = input.sort()
```
### copy
Works as specified

### filter
```python
from src.list_extensions import List

input = List.from_values(3, 6, 1, 2, 9)

# instead of
filter(lambda x: x % 2 == 0, input)
# or
[x for x in input if x % 2 == 0]
# write
input.filter(lambda x: x % 2 == 0)
```

### deepcopy
```python
from src.list_extensions import List

input = List.from_values(3, 6, 1, 2, 9)

# instead of
import copy
copy.deepcopy(input)
# write
input.deepcopy()
```

Every action takes place in it's own line, completely coherent and it reads from
left-to-right, top-to-bottom.
