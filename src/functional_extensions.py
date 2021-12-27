import copy
from abc import ABC, abstractmethod


# Abstract Base Classes

class Object(ABC):
    @classmethod
    def init(cls, instance):
        return cls(instance)

    def pipe(self, function, *args, **kwargs):
        return function(self, *args, **kwargs)

    def fe_copy(self, *args, **kwargs):
        return self.init(copy.copy(self))

    def fe_deepcopy(self, *args, **kwargs):
        return self.init(copy.deepcopy(self))


class Container(Object, ABC):
    pass


class Iterable(Object, ABC):
    def to_list(self):
        return List(self)

    def map(self, function):
        return Map(function, self)

    def min(self):
        return min(self)

    def max(self):
        return max(self)

    def sum(self):
        return sum(self)

    def fe_sorted(self, *args, **kwargs):
        """Sorts the Iterable by calling the builtin sorted function and
        returns the sorted list"""
        return List(sorted(self, *args, **kwargs))

    def enumerate(self, *args, **kwargs):
        return Enumerate(self, *args, **kwargs)

    def zip(self, *args, **kwargs):
        return Zip(self, *args, **kwargs)

    def all(self):
        return all(self)

    def any(self):
        return any(self)

    def for_each(self, apply, *args, **kwargs):
        """Applies a function to each element of the list and returns the
        list"""
        for x in self:
            apply(x)
        return self


class Iterator(Iterable, ABC):
    pass


class Reversible(ABC):
    def fe_reverse(self):
        return self.init(reversed(self))


class Sized(ABC):
    def len(self):
        return len(self)


class Collection(Sized, Iterable, Container, ABC):
    pass


class Sequence(Reversible, Collection, ABC):
    pass


class MutableSequence(Sequence, ABC):
    def map_inplace(self, apply, *args, **kwargs):
        """Projects each element of the List to a new element and mutates the
        list in place."""
        i = 0
        for item in iter(self):
            self[i] = apply(item)
        return self


class Mapping(Collection, ABC):
    pass


# Implementations

class List(MutableSequence, list):
    @classmethod
    def from_values(cls, *args, **kwargs):
        """Allows creating a List object from an arbitrary number of arguments
        instead of passing a normal list to __init__"""
        return List(list(args))

    def fe_sort(self, *args, **kwargs):
        """sorts the list inplace and returns it"""
        super().sort(*args, **kwargs)
        return self

    def filter(self, condition, *args, **kwargs):
        """Creates and returns a new list with only those elements of the
        current list that pass the condition. """
        return List.init([x for x in self if condition(x)])


class Dict(Mapping, dict):
    pass


class Set(Collection, set, ):
    pass


class Map(Iterator, map):
    pass


class Enumerate(Iterator, enumerate):
    pass


class Zip(Iterator, zip):
    pass


class Tuple(Sequence, tuple):
    pass
