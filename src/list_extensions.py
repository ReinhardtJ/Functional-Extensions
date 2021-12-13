from typing import Callable, Generic, TypeVar

T = TypeVar('T')
U = TypeVar('U')


class List(list, Generic[T]):
    def map(self, apply: Callable[[T], U]) -> 'List[U]':
        return List([apply(x) for x in self])

    def for_each(self, apply: Callable[[T], None]) -> None:
        for x in self:
            apply(x)

    def sort(self, *args, **kwargs) -> 'List[T]':
        super().sort(*args, **kwargs)
        return self

    def copy(self) -> 'List[T]':
        return List(super().copy())

    def filter(self, condition: Callable[[T], bool]) -> 'List':
        return List([x for x in self if condition(x)])


test_list = List([4, 1, 2, 3])

# traditional way
c = list(filter(lambda x: x > 2, (map(lambda x: x * x, test_list.copy()))))
c.sort()
for x in c:
    print(x)

# list comprehension
c = [x * x for x in test_list if x * x > 2]
c.sort()
for x in c:
    print(x)

# list extensions
test_list.map(lambda x: x * x)\
         .sort()\
         .filter(lambda x: x > 2)\
         .for_each(print)
