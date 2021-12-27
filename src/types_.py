import typing
from abc import abstractmethod, ABC
from typing import TypeVar

# Type Vars

T = TypeVar('T')
R = TypeVar('R')
K = TypeVar('K')
V = TypeVar('V')


# Base Class Interfaces

class ExtendedObject(typing.Generic[T], ABC):
    """Abstract base class for all Extended Object implementations"""

    @staticmethod
    @abstractmethod
    def init(self, instance: T) -> T:
        """static constructor for all extended objects. Needed so that we
        can immediately wrap intermediate regular objects"""

    @abstractmethod
    def pipe(self: T, fun: typing.Callable[[T, ...], R], *args, **kwargs) -> R:
        """Applies a function to this object and returns the result"""
        pass

    @abstractmethod
    def fe_copy(self: T, *args, **kwargs) -> T:
        """Copies the list by calling the build in copy function and returns the
        copy"""
        pass

    @abstractmethod
    def fe_deepcopy(self: T, *args, **kwargs) -> T:
        """Copies the list deeply by calling the deepcopy function from the copy
        module and returns the copy"""
        pass


class ExtendedContainer(ExtendedObject, typing.Generic[T], ABC):
    pass


class ExtendedIterable(ExtendedObject,
                       ABC, typing.Generic[T], typing.Iterable):
    def to_list(self: 'ExtendedIterable[T]') -> 'ExtendedList[T]':
        pass


class ExtendedIterator(ExtendedIterable, ABC, typing.Generic[T], typing.Iterator):
    pass


class ExtendedSized(ABC, typing.Generic[T], typing.Sized):
    pass


class ExtendedCollection(ExtendedSized, ExtendedIterable, ExtendedContainer,
                         ABC, typing.Generic[T], typing.Collection):
    pass


class ExtendedReversible(ExtendedIterable,
                         ABC, typing.Generic[T], typing.Reversible):
    pass


class ExtendedSequence(ExtendedReversible, ExtendedCollection,
                       ABC, typing.Generic[T], typing.Sequence):
    pass


class ExtendedMutableSequence(ExtendedSequence,
                              ABC, typing.Generic[T], typing.MutableSequence):
    pass


# Implementation Interfaces


class ExtendedList(ExtendedMutableSequence,
                   ABC, typing.Generic[T], typing.List):
    pass


class ExtendedMapping(ExtendedCollection,
                      ABC, typing.Generic[K, V], typing.Mapping):
    pass


class ExtendedDict(ExtendedMapping,
                   ABC, typing.Generic[K, V], typing.Dict):
    pass


class ExtendedSet(ExtendedCollection,
                  ABC, typing.Generic[T], typing.Set):
    pass


class ExtendedMap(ExtendedIterator,
                  ABC, typing.Generic[T]):
    pass


class ExtendedEnumerate(ExtendedIterator,
                        ABC, typing.Generic[T]):
    pass


class ExtendedZip(ExtendedIterator,
                  ABC, typing.Generic[T]):
    pass


class ExtendedTuple(ExtendedSequence,
                    ABC, typing.Generic[T]):
    pass
