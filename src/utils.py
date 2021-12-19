from src.functional_extensions import Iterable, Map
from src.types_ import T


def map(iterable: Iterable[T], function) -> Iterable[T]:
    return Map(function, iterable)
