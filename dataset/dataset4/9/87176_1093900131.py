
from abc import ABC, abstractmethod
from functools import wraps

class A(ABC):
    @abstractmethod
    def f(self):
        pass
    
    @wraps(f)
    def wrapper(self):
        print('f is called!')
        f()
        
class B(A):
    def f(self):
        print('f!')

B()
