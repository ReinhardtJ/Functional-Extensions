import collections
import copy
import typing
from abc import ABC

from src.functional_extensions import List, Map, Enumerate, Zip
from src.types_ import U, T, IObject, IContainer


class Object(IObject, typing.Generic[T], ABC):
    def pipe(self: T, fun: typing.Callable[[T, ...], U], *args, **kwargs) -> U:
        return fun(self, *args, **kwargs)

    def fe_copy(self: T, *args, **kwargs) -> T:
        return type(self)(copy.copy(self))

    def fe_deepcopy(self: T, *args, **kwargs) -> T:
        return type(self)(copy.deepcopy(self))


class Container(Object, IContainer, typing.Generic[T]):
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
        return Enumerate(self, *args, **kwargs)

    def zip(self, *args, **kwargs):
        return Zip(self, *args, **kwargs)

    def all(self) -> bool:
        return all(self)

    def any(self) -> bool:
        return any(self)

    def for_each(self, apply: typing.Callable[[T], None], *args, **kwargs) -> 'Iterable[T]':
        """Applies a function to each element of the list and returns the
        list"""
        for x in self:
            apply(x)
        return self


class Iterator(Iterable, ABC, typing.Generic[T]):
    pass


class Sized(typing.Sized, ABC, typing.Generic[T]):
    def len(self):
        return len(self)


class Collection(Sized, Iterable, Container, typing.Collection, ABC, typing.Generic[T]):
    pass


class Reversible(Iterable, typing.Reversible, ABC, typing.Generic[T]):
    def fe_reverse(self) -> 'Reversible[T]':
        c = copy.copy(self)
        # TODO(Jonas): check how we can initialize this better. Maybe a static initializor that has to be overwritten
        # by all subclasses in Object?
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
