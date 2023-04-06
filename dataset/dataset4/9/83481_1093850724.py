from dataclasses import dataclass


@dataclass
class A:
    PARAM: int


@dataclass
class B(A):
    ARG: int
    PARAM: int = 1