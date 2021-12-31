import copy
import inspect
import types
import typing
from itertools import filterfalse
import funcy


# Abstract Base Classes

class Object:
    def _pipe(self, function, *args, **kwargs): return function(self, *args, **kwargs)
    def _copy(self): return copy.copy(self)
    def _deepcopy(self, *args, **kwargs): return copy.deepcopy(self)
    def _type(self): return type(self)


class Function(Object, typing.Callable):
    @classmethod
    def init(cls, instance):
        f = Function()
        f.__call__ = instance
        return f

    def _compose(self, function):
        return Function.init(funcy.compose(self, function))


class Container(Object, typing.Container):
    pass


class Iterable(Object, typing.Iterable):
    def _to_list(self): return List(self)
    def _to_set(self): return Set(self)
    def _to_tuple(self): return Tuple(self)

    def _map(self, function, *args, **kwargs):
        ctor = initializers[type(self)]
        return ctor(function(element, *args, **kwargs) for element in self)

    def _for_each(self, function, *args, **kwargs):
        for x in self:
            function(x, *args, **kwargs)
        return self

    def _min(self): return min(self)
    def _max(self): return max(self)
    def _sum(self): return sum(self)
    def _all(self): return all(self)
    def _any(self): return any(self)
    def _enumerate(self, start=0): return Enumerate(self, start=start)
    def _zip(self, *iterables): return Zip(self, *iterables)

    def _sort(self, key=None, reverse=False):
        return List(sorted(self, key=key, reverse=reverse))
    def _filter(self, condition):
        ctor = initializers[type(self)]
        return ctor(filter(condition, self))

    def _filterfalse(self, condition):
        ctor = initializers[type(self)]
        return ctor(filterfalse(condition, self))


class Iterator(Iterable, typing.Iterator):
    pass


class Reversible(Object, typing.Reversible):
    def _reverse(self):
        ctor = initializers[type(self)]
        return ctor(reversed(self))


class Sized(Object, typing.Sized):
    def _len(self): return len(self)


class Collection(Sized, Iterable, Container, typing.Collection):
    pass


class Sequence(Reversible, Collection, typing.Sequence):
    pass


class MutableSequence(Sequence, typing.MutableSequence):
    def _map_inplace(self, apply, *args, **kwargs):
        """Projects each element of the List to a new element and mutates the
        list in place."""
        for i, item in enumerate(iter(self)):
            self[i] = apply(item, *args, *kwargs)
        return self


class Mapping(Collection, typing.Mapping):
    pass


# Implementations

class List(list, MutableSequence, typing.List):
    def _sort_inplace(self, key=None, reverse=False):
        """sorts the list inplace and returns it"""
        super().sort(key=key, reverse=reverse)
        return self


class Dict(dict, Mapping, typing.Dict):
    pass


class Set(set, Collection, typing.Set):
    pass


class Map(map, Iterator):
    pass


class Enumerate(enumerate, Iterator):
    pass


class Zip(zip, Iterator):
    pass


class Tuple(tuple, Sequence, typing.Tuple):
    pass


def monkey_patch_bound_methods(cls, instance):
    """Helper function to easily extend objects without having to change their
    classes by monkey-patching the extended functions"""
    methods = [member for member in inspect.getmembers(cls)
               if not member[0].startswith('__')]
    for method in methods:
        if hasattr(instance, method[0]):
            raise AttributeError(f'cannot extend {instance}, because it already has'
                             f'a method called {method[0]}')
        setattr(instance, method[0], types.MethodType(method[1], instance))
    return instance


_t = Tuple
_m = Map
_s = Set
_d = Dict
def _l(*values):
    # case _l is called with a container or iterable instance
    if len(values) == 1 and isinstance(values[0], (typing.Container, typing.Iterable)):
        return List(values[0])
    # case _l is called with multiple individual values
    return List(values)
_f = Function.init
_o = funcy.partial(monkey_patch_bound_methods, Object)

initializers = {
    Tuple: _t,
    Map: _m,
    Set: _s,
    Dict: _d,
    List: _l,
}