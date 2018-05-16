from typing import Optional, Union


class Employee:
    ...


def handle_optional_employee_a(e: Union[Employee, None]):
    ...


def handle_optional_employee_b(e: Employee = None):  # Optionality automatically assumed
    ...


def handle_optional_employee_c(e: Optional[Employee]):
    ...
