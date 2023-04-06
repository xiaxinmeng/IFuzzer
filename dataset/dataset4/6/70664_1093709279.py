# File models/a.py
from models import b
class A(Model):
    def foo(self, b: 'b.B'): ...

# File models/b.py
from models import a
class B(Model):
    def bar(self, a: 'a.A'): ...

# File main.py
from models.a import A
from models.b import B