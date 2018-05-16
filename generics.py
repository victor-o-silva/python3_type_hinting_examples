from typing import Any, Sequence, TypeVar

T = TypeVar('T')


def first(l: Sequence[T]) -> T:
    return l[0]


# Constrained types

AnyStr = TypeVar('AnyStr', str, bytes)


def concat(x: AnyStr, y: AnyStr) -> AnyStr:
    return x + y


# Any type

def count_truthy(elements: Sequence[Any], count_falsy_instead: bool=False) -> int:
    return sum(1 for elem in elements if bool(elem) is not count_falsy_instead)
