from typing import Callable, Iterable


def async_query(process_ages: Callable[[Iterable[int]], bool]) -> None:
    ages = [10, 20, 30, 40, 50]
    process_ages(ages)


def print_ages(ages: Iterable[int]) -> bool:
    for age in ages:
        print(age)
    return True


async_query(print_ages)


# Without specifying callable signature

def call(func: Callable[..., str]):
    res = func('some', 'params')
    print(f'Called {func.__name__}, which returned {res!r}')


call(lambda *args, **kwargs: 'TESTING')
