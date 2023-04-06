from typing import Generic, TypeVar
import pickle

T = TypeVar("T")


class A(Generic[T]):
    def __init__(self, x: T):
        self.x = x


class B(A[str]):
    def __init__(self, x: str):
        self.x = x


b = B("hello")
z = pickle.dumps(b)
print(z)
_ = pickle.loads(z)