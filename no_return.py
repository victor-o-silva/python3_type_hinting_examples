import sys
from typing import NoReturn


def raises_exception(errors_count) -> NoReturn:
    if errors_count:
        sys.exit(1)
    else:
        sys.exit(0)
