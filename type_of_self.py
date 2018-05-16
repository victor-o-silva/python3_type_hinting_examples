from typing import TypeVar

T = TypeVar('T', bound='Copyable')


class Copyable:
    value = None

    def __init__(self, value=None):
        self.value = value

    def copy(self: T) -> T:
        return Copyable(self.value)
