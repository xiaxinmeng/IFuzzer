from pathlib import Path
from unittest.mock import patch


class TestException(MemoryError):
    pass


class report_ctx:
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, tb):
        report(exc_value)


class raises:
    def __init__(self, ex):
        self.ex = ex
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, tb):
        return issubclass(exc_type, self.ex)


def report(ex):
    pass


def error():
    raise MemoryError


modname = Path(__file__).stem

for _ in range(10):
    with patch(f"{modname}.report"):
        with raises(MemoryError), report_ctx():
            raise MemoryError

        with raises(TestException):
            raise TestException

        with raises(MemoryError):
            error()