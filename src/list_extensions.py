import copy
from typing import Callable, Generic, TypeVar, Any, Tuple

T = TypeVar('T')
U = TypeVar('U')


class List(list, Generic[T]):
    @classmethod
    def from_values(cls, *args) -> 'List[T]':
        """Allows creating a List object from an arbitrary number of arguments
        instead of passing a normal list to __init__"""
        return cls(list(args))

    def map(self, apply: Callable[[T], U]) -> 'List[U]':
        """Projects each element of the List to an element of a new list by
        applying a function and returns the new list"""
        return List([apply(x) for x in self])

    def for_each(self, apply: Callable[[T], None]) -> 'List[T]':
        """Applies a function to each element of the list and returns the
        list"""
        for x in self:
            apply(x)
        return self

    def sort(self, *args, **kwargs) -> 'List[T]':
        """Sorts the list by calling the built in sort function and returns
        the sorted list"""
        return self.copy().sort(*args, **kwargs)

    def copy(self) -> 'List[T]':
        """Copies the list by calling the build in copy function and returns the
        copy"""
        return List(super().copy())

    def filter(self, condition: Callable[[T], bool]) -> 'List':
        """Creates and returns a new list with only those elements of the
        current list that pass the condition. """
        return List([x for x in self if condition(x)])

    def deepcopy(self) -> 'List[T]':
        """Copies the list deeply by calling the deepcopy function from the copy
        module and returns the copy"""
        return copy.deepcopy(self)

