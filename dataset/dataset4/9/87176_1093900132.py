from abc import ABC, abstractmethod
from functools import wraps

class A(ABC):
    @abstractmethod
    def f(self):
        pass

    def __init_subclass__(cls, **class_kwargs):
        old_f = cls.f
        @wraps(old_f)
        def wrapper(*args, **kwargs):
            print("f is called!")
            old_f(*args, **kwargs)
        cls.f = wrapper
        super().__init_subclass__()

class B(A):
    def f(self):
        print('f!')

class C(A):
    pass