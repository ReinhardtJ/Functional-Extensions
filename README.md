# Functional Extensions
for Python

This repository aims to extend the Python programming language by adding some
known, concepts from other popular programming languages. Most of those concepts
are known from languages that support functional programming.

- being able to chain both pure and mutating functions by calling them directly 
  on objects
- applying functions to objects and chaining them through a pipe-function
- composing functions (not yet implemented)

## Usage

```python
# initialize an extended list by either passing a regular list to __init__ or 
# calling the from_values function

from src.functional_extensions import List

regular_list = [1, 2, 3, 4]
extended_list_1 = List([1, 2, 3, 4])
extended_list_2 = List.from_values(1, 2, 3, 4)
assert regular_list == extended_list_1 == extended_list_2
```
## Available functions
### map

```python
from src.functional_extensions import List

input = List.from_values(3, 6, 1, 2, 9)

# instead of
map(lambda x: x ** 2, input)
# or
[x ** 2 for x in input]
# write
input.map(lambda x: x ** 2)
```
### for_each

```python
from src.functional_extensions import List

input = List.from_values(3, 6, 1, 2, 9)

# instead of
for i in input:
    print(i)
# write
input.for_each(print)
```
### sort

```python
from src.functional_extensions import List

input = List.from_values(3, 6, 1, 2, 9)

# instead of
sorted = input.copy().fe_sorted()
# write
sorted = input.fe_sorted()
```
### copy
Works as specified

### filter

```python
from src.functional_extensions import List

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
from src.functional_extensions import List

input = List.from_values(3, 6, 1, 2, 9)

# instead of
import copy

copy.deepcopy(input)
# write
input.deepcopy()
```

Every action takes place in it's own line, completely coherent and it reads from
left-to-right, top-to-bottom.
