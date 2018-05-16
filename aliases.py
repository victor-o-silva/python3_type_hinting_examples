from typing import Iterable, Tuple, TypeVar

N = TypeVar('N', int, float, complex)
Point = Tuple[N, N]
Vector = Iterable[Point]


def get_vector() -> Vector:
    return [(1, 2), (3, 4), (5, 6)]


def in_product(v: Vector) -> N:
    return sum(x * y for x, y in v)
