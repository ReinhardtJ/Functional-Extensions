# Functional Extensions
for Python

This repository aims to extend the Python programming language by adding some
known concepts from other popular programming languages. Most of those concepts
are known from languages that support functional programming.

- being able to chain pure (and mutating) functions by calling them directly 
  on objects. Most of those functions are known from the built-in functions.
  
- applying functions to objects and chaining them through a pipe-function
- composing functions (not yet implemented)

## Usage

```
import functional_extensions as fe

regular_list = [1, 2, 3, 4]
extended_list = fe.List.from_values(1, 2, 3, 4)

# all extended classes implement the init()-method. These are used to extend
# the built-in, regular objects
extended_list = fe.List.init([1, 2, 3, 4])
extended_set = fe.Set.init(set(1, 2, 3, 4))
extended_dict = fe.Dict.init({'key': 'value'})
extended_tuple = fe.Tuple.init((1, 2, 3, 4))

# In addition to Lists, Tuples and Sets also support using from_values()
```
## Available functions
### Object
```
init(cls, instance)
```

Initializes an extended object from the instance of a built-in object.

---

``` 
pipe(self, function, *args, **kwargs)
``` 

Applies the object `self` to a function `function` with the arguments from `*args` 
and `**kwarngs` and returns the result.

---

```
fe_copy(self) 
fe_deepcopy(self)
``` 

Copies `self`, either shallowly or deeply, and returns the result.

---

```
type(self)
```

Returns `type(self)`.

### Iterable

```
to_list(self)
to_set(self)
to_tuple(self)
```

Converts the iterable `self` into the desired object.

---

```
map(self, function)
```

Applies every element of `self` to `function` and returns an iterable of the new
elements.

---

```
fe_map(self, function, *args, **kwargs)
```

Similar to `map`, but you can additionally pass `*args` and `**kwargs` to the
map-`function`. 

The main difference is, that `fe_map` returns an instance of the
same type that `self` is, and not a new `Map`-instance

---

```
for_each(self, apply, *args, **kwargs)
```

For every element in `self`, `function` is called with said element, as well
as `*args` and `**kwargs`. The list is then returned.

---

```
min(self)
max(self)
sum(self)
all(self)
any(self)
```


Returns `min(self)`, `max(self)`, `sum(self)`, `all(self)` and `any(self)` respectively.

--- 

```
fe_sort(self, key=None, reverse=False)
```

Sorts all elements from the iterable `self` in a new list and returns it. Calls
the `sorted`-function under the hood with `key` and `reverse`.

---

`enumerate(self, start=0)`

Returns an enumerate object from the iterable `self`.

--- 

`zip(self, *iterables)`

Iterates over `self` and all iterables in `*iterables`, producing tuples with
an item from each one.

--- 

```
filter(self, condition)
filterfalse(self, condition)
```

`filter` returns a new instance of this iterable with only the elements that
`condition` returns true.

`filterfalse`returns a new instance of this iterable
with only the elements that `condition` returns false.

### Reversible

```
fe_reverse(self)
```

Returns a new instance of the reversed iterable `self`.

### Sized

```
len(self)
```

Returns `len(self)`

### MutableSequence

```
map_inplace(self, apply, *args, **kwargs)
```

Applies every element of `self` to `function` and overwrites this element with
the new value.


### List

```
from_values(cls, *values)
```

Creates a new list from the values in `*values`.

---

```
fe_sort_inplace(self, key=None, reverse=False)
```

Sorts the list in-place and returns the sorted list

### Set

```
from_values(cls, *values)
```

Creates a new set from the values in `*values`.

### Tuple

```
from_values(cls, *values)
```

Creates a new tuple from the values in `*values`.

## Examples

Most of those functions should not need additional examples, as they are a mere
re-phrasing of some basic concepts and funtions of the Python programming 
language. 

f you need an example anyway, you should consider looking at the test
classes, which cover every function.


## The why
An excerpt of the "zen of python":

> Beautiful is better than ugly

A simple exercise. Initialize a list with the numbers `[4, 1, 2, 3]`, take the negative
square of these numbers, sort the list and print every element individually.

Which one of the following code pieces is more beautiful?
```python
input = [4, 1, 2, 3]
squared = [-(x ** 2) for x in input]
squared.sort()
for element in squared:
  print(x)
```

```python
def negative_square(x): return - (x ** 2)

fe.List.from_values(4, 1, 2, 3)\
       .map_inplace(negative_square)\
       .fe_sort()\
       .for_each(print)
```

There are 4 things happening. In the top example, all things are expressed via
a slightly different syntax. Initialization with a list literal, mapping by a 
list comprehension, calling the sort-function on the list and then printing all
elements 

In the bottom example, every "thing" that is happening, is expressed in a 
coherent way - by calling a function.

| Requirement                                       | Corresponding Function                       |
|---------------------------------------------------|----------------------------------------------|
| Initialize a list with the numbers `[4, 1, 2, 3]` | `.from_values(4, 1, 2, 3)`                   |
| Take the negative square                          | `.map_inplace(negative_square)` <sup>1</sup> |
| Sort the list                                     | `.fe_sort()`                                 |
| Print every element individually                  | `.for_each(print)`                           |

<sup>1</sup> we could also use a lambda-function in-place to avoid having to
declare an own function for this case. However, the code might become slightly
more expressive. Which brings us to the next "principle"

> Explicit is better than implicit

This principle means, that there shouldn't be anything unexpected happening under
the hood, which is often the case in high-level codebases. Metaprogramming,
making use of inheritance or just not choosing proper variable names can make
the code hard to read and understand, making it more easy to make mistakes.

These extensions might make things more complex at first glance, but the naming
is chosen quite carefully. If a function name corresponds to a name of a
built-in function, this functions will not do more or less than exactly that
function.

All other functions are designed to be pure, and not cause anything to happen
outside of their little scope.

All function that are not pure, are explicitly named like that, for example
`map_inplace`

All functions that have similar names than built-in functions, have an 
explicit "fe_"-prefix to denote that they do things differently, for example
`fe_sort`, which adheres to the rule that functions are pure, unlike the `sort()`-
function from the builtin `list`-class.

> Simple is better than complex

and

> Readability counts
 
One might argue, that any code which doesn't directly solves a certain use case
is, by definition, not simple. It might be correct to define complexity like that.
But you can also define complexity by how much time it takes you to read and 
understand code. This library tries to help reduce complexity of the code itself,
on a less abstract layer than the use-case-specific solutions are written in. By
that, hopefully those solutions also become less complex.

> There should be one-- and preferably only one --obvious way to do it.

Yes, in an attempt to fulfill other principles, this principle is arguably 
broken. Now there is one more way to write a for-loop or call a map-function.
At least I try to keep this rule fulfilled within this library. There should
be one obvious way to do one thing by using functional extensions.

