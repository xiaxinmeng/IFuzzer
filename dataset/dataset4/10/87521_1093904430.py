
#from __future__ import annotations
from inspect import Parameter, signature


def foo(x: str) -> str:
    return x + x


def test_foo():
    expected = (
        Parameter("x", Parameter.POSITIONAL_OR_KEYWORD, annotation=str),
    )

    actual = tuple(signature(foo).parameters.values())

    assert expected == actual
