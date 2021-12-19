import collections
import copy
from typing import Callable, Generic, Any

from abc import ABC

from src.types_ import T, U


class Object:
    def pipe(self, fun: Callable[[Any, ...], U], *args, **kwargs) -> U:
        return fun(self, *args, **kwargs)


class Iterable(Object, collections.Iterable, ABC):
    def to_list(self):
        return List(self)


class Iterator(Iterable, ABC):
    pass


class Map(map, Iterator):
    pass


class List(list, Iterator, Generic[T]):
    @classmethod
    def from_values(cls, *args, **kwargs) -> 'List[T]':
        """Allows creating a List object from an arbitrary number of arguments
        instead of passing a normal list to __init__"""
        return cls(list(args))

    def map(self, apply: Callable[[T], U], *args, **kwargs) -> 'List[U]':
        """Projects each element of the List to an element of a new list by
        applying a function and returns the new list"""
        return List([apply(x) for x in self])

    def map_inplace(self, apply: Callable[[T], U], *args, **kwargs) -> 'List[U]':
        """Projects each element of the List to a new element and mutates the
        list in place."""
        for i in range(len(self)):
            self[i] = apply(self[i])
        return self

    def for_each(self, apply: Callable[[T], None], *args, **kwargs) -> 'List[T]':
        """Applies a function to each element of the list and returns the
        list"""
        for x in self:
            apply(x)
        return self

    def sort(self, *args, **kwargs) -> 'List[T]':
        """Sorts the list by calling the built in sort function and returns
        the sorted list"""
        return List(sorted(self, *args, **kwargs))

    def sort_inplace(self, *args, **kwargs) -> 'List[T]':
        super().sort()
        return self

    def copy(self, *args, **kwargs) -> 'List[T]':
        """Copies the list by calling the build in copy function and returns the
        copy"""
        return List(super().copy())

    def filter(self, condition: Callable[[T], bool], *args, **kwargs) -> 'List':
        """Creates and returns a new list with only those elements of the
        current list that pass the condition. """
        return List([x for x in self if condition(x)])

    def deepcopy(self, *args, **kwargs) -> 'List[T]':
        """Copies the list deeply by calling the deepcopy function from the copy
        module and returns the copy"""
        return copy.deepcopy(self)
