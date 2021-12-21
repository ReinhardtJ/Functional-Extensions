import collections
import copy
import typing
from abc import ABC

from src.types_ import T, U


class Object(ABC):
    def pipe(self, fun: typing.Callable[..., U], *args, **kwargs) -> U:
        return fun(self, *args, **kwargs)


class Container(typing.Container, ABC, typing.Generic[T]):
    pass


class Iterable(Object, collections.Iterable, ABC, typing.Generic[T]):
    def to_list(self):
        return List(self)

    def map(self, function: typing.Callable[[T], U], *args, **kwargs) -> 'Map[U]':
        """Projects each element of the List to an element of a new list by
        applying a function and returns the new list"""
        return Map(function, self)

    def min(self) -> T:
        return min(self)

    def max(self) -> T:
        return max(self)

    def sum(self) -> T:
        return sum(self)

    def fe_sorted(self, *args, **kwargs) -> 'List[T]':
        """Sorts the Iterable by calling the builtin sorted function and
        returns the sorted list"""
        return List(sorted(self, *args, **kwargs))

    def enumerate(self, *args, **kwargs):
        return enumerate(self, *args, **kwargs)


class Iterator(Iterable, ABC, typing.Generic[T]):
    pass


class Sized(typing.Sized, ABC, typing.Generic[T]):
    def len(self):
        return len(self)


class Collection(Sized, Iterable, Container, typing.Collection, ABC, typing.Generic[T]):
    pass


class Reversible(Iterable, typing.Reversible, ABC, typing.Generic[T]):
    def fe_reverse(self) -> 'Reversible[T]':
        return type(self)(reversed(self))


class Sequence(Reversible, Collection, typing.Sequence, ABC, typing.Generic[T]):
    pass


class MutableSequence(Sequence, typing.MutableSequence, ABC, typing.Generic[T]):
    def map_inplace(self, apply: typing.Callable[[T], U], *args, **kwargs) -> 'Iterable[U]':
        """Projects each element of the List to a new element and mutates the
        list in place."""
        i = 0
        for item in iter(self):
            self[i] = apply(item)
        return self


class List(list, MutableSequence, typing.Generic[T]):
    @classmethod
    def from_values(cls, *args, **kwargs) -> 'List[T]':
        """Allows creating a List object from an arbitrary number of arguments
        instead of passing a normal list to __init__"""
        return cls(list(args))

    def for_each(self, apply: typing.Callable[[T], None], *args, **kwargs) -> 'List[T]':
        """Applies a function to each element of the list and returns the
        list"""
        for x in self:
            apply(x)
        return self


    def fe_sort(self, *args, **kwargs) -> 'List[T]':
        """sorts the list inplace and returns it"""
        super().sort()
        return self

    def copy(self, *args, **kwargs) -> 'List[T]':
        """Copies the list by calling the build in copy function and returns the
        copy"""
        return List(super().copy())

    def filter(self, condition: typing.Callable[[T], bool], *args, **kwargs) -> 'List':
        """Creates and returns a new list with only those elements of the
        current list that pass the condition. """
        return List([x for x in self if condition(x)])

    def deepcopy(self, *args, **kwargs) -> 'List[T]':
        """Copies the list deeply by calling the deepcopy function from the copy
        module and returns the copy"""
        return copy.deepcopy(self)




class Map(map, Iterator, typing.Generic[T]):
    pass

