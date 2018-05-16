from typing import Union, Sequence


class Employee:
    ...


def handle_employees(e: Union[Employee, Sequence[Employee]]) -> None:
    if isinstance(e, Employee):
        e = [e]
        ...

