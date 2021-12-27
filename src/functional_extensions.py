import copy
import typing
from abc import ABC, abstractmethod


# Abstract Base Classes
from itertools import filterfalse


class Object(ABC):
    @classmethod
    def init(cls, instance):
        return cls(instance)

    def pipe(self, function, *args, **kwargs):
        return function(self, *args, **kwargs)

    def fe_copy(self):
        return self.init(copy.copy(self))

    def fe_deepcopy(self, *args, **kwargs):
        return self.init(copy.deepcopy(self))

    def type(self):
        return type(self)


class Container(Object, ABC, typing.Container):
    pass


class Iterable(Object, ABC, typing.Iterable):
    def to_list(self):
        return List(self)

    def to_set(self):
        return Set(self)

    def to_tuple(self):
        return Tuple(self)

    def map(self, function):
        return Map(function, self)

    def fe_map(self, function, *args, **kwargs):
        return self.init(function(element, *args, **kwargs) for element in self)

    def for_each(self, function, *args, **kwargs):
        for x in self:
            function(x, *args, **kwargs)
        return self

    def min(self):
        return min(self)

    def max(self):
        return max(self)

    def sum(self):
        return sum(self)

    def all(self):
        return all(self)

    def any(self):
        return any(self)

    def fe_sort(self, key=None, reverse=False):
        """Sorts the Iterable by calling the builtin sorted function and
        returns the sorted list"""
        return List(sorted(self, key=key, reverse=reverse))

    def enumerate(self, start=0):
        return Enumerate(self, start=0)

    def zip(self, *iterables):
        return Zip(self, *iterables)

    def filter(self, condition):
        """Creates and returns a new iterable with only those elements of the
        current iterable that pass the condition. """
        return self.init(filter(condition, self))

    def filterfalse(self, condition):
        """The inverse of filter. Keeps elements that do not pass the condition"""
        return self.init(filterfalse(condition, self))


class Iterator(Iterable, ABC, typing.Iterator):
    pass


class Reversible(Object, ABC, typing.Reversible):
    def fe_reverse(self):
        return self.init(reversed(self))


class Sized(Object, ABC, typing.Sized):
    def len(self):
        return len(self)


class Collection(Sized, Iterable, Container, ABC, typing.Collection):
    pass


class Sequence(Reversible, Collection, ABC, typing.Sequence):
    pass


class MutableSequence(Sequence, ABC, typing.MutableSequence):
    def map_inplace(self, apply, *args, **kwargs):
        """Projects each element of the List to a new element and mutates the
        list in place."""
        for i, item in enumerate(iter(self)):
            self[i] = apply(item, *args, *kwargs)
        return self


class Mapping(Collection, ABC, typing.Mapping):
    pass


# Implementations

class List(list, MutableSequence, typing.List):
    @classmethod
    def from_values(cls, *values):
        """Allows creating a List object from an arbitrary number of arguments
        instead of passing a normal list to __init__"""
        return List(list(values))

    def fe_sort_inplace(self, key=None, reverse=False):
        """sorts the list inplace and returns it"""
        super().sort(key=key, reverse=reverse)
        return self


class Dict(dict, Mapping, typing.Dict):
    pass


class Set(set, Collection, typing.Set):
    @classmethod
    def from_values(cls, *values):
        """Allows creating a Set object from an arbitrary number of arguments
        instead of passing a normal set to __init__"""
        return Set(set(values))


class Map(map, Iterator):
    pass


class Enumerate(enumerate, Iterator):
    pass


class Zip(zip, Iterator):
    pass


class Tuple(tuple, Sequence, typing.Tuple):
    @classmethod
    def from_values(cls, *values):
        """Allows creating a Tuple object from an arbitrary number of arguments
        instead of passing a normal tuple to __init__"""
        return Tuple(Tuple(values))
