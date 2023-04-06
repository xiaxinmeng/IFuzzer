
from abc import ABC, abstractmethod

class Base(ABC):
    @abstraabstractmethod
    def foo(self):
         pass

class A(Base, ABC):  # totally okay, because class directly inherits from ABC
     pass

class B(Base):  # will fail, because class doesn't implement foo method
    pass
