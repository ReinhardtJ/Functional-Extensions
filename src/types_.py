import typing
from abc import abstractmethod, ABC
from typing import TypeVar

T = TypeVar('T')
U = TypeVar('U')
K = TypeVar('K')
V = TypeVar('V')


class IObject(typing.Generic[T], ABC):
    @abstractmethod
    def pipe(self: T, fun: typing.Callable[[T, ...], U], *args, **kwargs) -> U:
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


class IContainer(IObject, typing.Container, typing.Generic[T], ABC):
    pass


class IIterable()
