from __future__ import annotations
from functools import singledispatchmethod


class Integer:
    def __init__(self, value: int):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

    @singledispatchmethod
    def add(self, other: object) -> Integer:
        raise NotImplementedError(f"Unsupported type {type(other)}")

    @add.register
    def _(self, other: int) -> "Integer":
        return Integer(self.value + other)