from typing import NamedTuple


class X(NamedTuple):
    a: str
    b: str

    # comment this out to remove the issue
    def foo(self):
        return super(X, self)