import copy
import typing
from abc import ABC

from src.base_classes import Iterator, Collection, MutableSequence, Sequence
from src.types_ import T, K, V


class List(list, MutableSequence, typing.Generic[T]):
    @classmethod
    def from_values(cls, *args, **kwargs) -> 'List[T]':
        """Allows creating a List object from an arbitrary number of arguments
        instead of passing a normal list to __init__"""
        return cls(list(args))



    def fe_sort(self, *args, **kwargs) -> 'List[T]':
        """sorts the list inplace and returns it"""
        super().sort()
        return self


    def filter(self, condition: typing.Callable[[T], bool], *args, **kwargs) -> 'List':
        """Creates and returns a new list with only those elements of the
        current list that pass the condition. """
        return List([x for x in self if condition(x)])


class Mapping(Collection, ABC):
    pass


class Dict(dict, Mapping, typing.Generic[K, V]):
    pass


class Set(set, Collection, typing.Generic[T]):
    pass


class Map(map, Iterator, typing.Generic[T]):
    pass


class Enumerate(enumerate, Iterator, typing.Generic[T]):
    pass


class Zip(zip, Iterator, typing.Generic[T]):
    pass


class Tuple(tuple, Sequence, typing.Generic[T]):
    pass
