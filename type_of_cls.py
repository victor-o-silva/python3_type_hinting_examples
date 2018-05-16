from typing import Type, TypeVar

T = TypeVar('T', bound='MyClass')


class MyClass:
    @classmethod
    def factory(cls: Type[T]) -> T:
        return MyClass()
