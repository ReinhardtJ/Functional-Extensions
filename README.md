# List-Extensions

Use lists in Python just like you're used to. Be it Java Streams, C# LINQ 
Extensions or the JavsScript array prototype functions.

Instead of
```python
input = [3, 6, 1, 2, 9]

intermediate = [x ** 2 for x in input if x ** 2 % 2 == 0]
intermediate.sort()
for entry in intermediate:
    print(entry)
```
Write this:
```python
input = [3, 6, 1, 2, 9]

input.map(lambda x: x**2)\
     .sort()\
     .filter(lambda x: x % 2 == 0)\
     .for_each(print)
```
Every action takes place in it's own line, completely coherent and it reads from
left-to-right, top-to-bottom.