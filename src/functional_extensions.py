import copy
import typing
from abc import ABC

from src.types_ import T, K, V, ExtendedList, ExtendedMapping, ExtendedDict, ExtendedSet, ExtendedMap, \
    ExtendedEnumerate, ExtendedZip, ExtendedTuple, ExtendedObject, R, ExtendedContainer, ExtendedIterable, \
    ExtendedIterator, ExtendedSized, ExtendedCollection, ExtendedReversible, ExtendedSequence, ExtendedMutableSequence


class Object(ExtendedObject,
             typing.Generic[T], ABC):
    def pipe(self: T, fun: typing.Callable[[T, ...], R], *args, **kwargs) -> R:
        return fun(self, *args, **kwargs)

    def fe_copy(self: T, *args, **kwargs) -> T:
        return type(self)(copy.copy(self))

    def fe_deepcopy(self: T, *args, **kwargs) -> T:
        return type(self)(copy.deepcopy(self))


class Container(Object,
                ExtendedContainer,
                typing.Generic[T], ABC):
    pass


class Iterable(Object, ExtendedIterable,
               ABC, typing.Generic[T]):
    def to_list(self):
        return List(self)

    def map(self, function: typing.Callable[[T], R], *args, **kwargs) -> ExtendedMap[R]:
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


class Reversible(ExtendedReversible,
                 Iterable,
                 ABC, typing.Generic[T]):
    def fe_reverse(self) -> 'Reversible[T]':
        c = copy.copy(self)
        # TODO(Jonas): check how we can initialize this better. Maybe a static initializor that has to be overwritten
        # by all subclasses in Object?
        return type(self)(reversed(self))


class Sized(ExtendedSized,
            ABC, typing.Generic[T]):
    def len(self):
        return len(self)


class Collection(ExtendedCollection,
                 Sized, Iterable, Container,
                 ABC, typing.Generic[T]):
    pass


class Sequence(ExtendedSequence,
               Reversible, Collection,
               ABC, typing.Generic[T], ):
    pass


class MutableSequence(ExtendedMutableSequence,
                      Sequence,
                      ABC, typing.Generic[T]):
    def map_inplace(self, apply: typing.Callable[[T], R], *args, **kwargs) -> 'Iterable[R]':
        """Projects each element of the List to a new element and mutates the
        list in place."""
        i = 0
        for item in iter(self):
            self[i] = apply(item)
        return self


class List(ExtendedList, list, MutableSequence,
           typing.Generic[T]):
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



class Mapping(ExtendedMapping, Collection,
              ABC, typing.Generic[K, V]):
    pass


class Dict(ExtendedDict, dict, Mapping,
           typing.Generic[K, V]):
    pass


class Set(ExtendedSet, set, Collection,
          typing.Generic[T]):
    pass


class Iterator(Iterable, ExtendedIterator,
               ABC, typing.Generic[T]):
    pass


class Map(ExtendedMap, map, Iterator,
          typing.Generic[T]):
    pass


class Enumerate(ExtendedEnumerate, enumerate, Iterator,
                typing.Generic[T]):
    pass


class Zip(ExtendedZip, zip, Iterator,
          typing.Generic[T]):
    pass


class Tuple(ExtendedTuple, tuple, Sequence,
            typing.Generic[T]):
    pass


