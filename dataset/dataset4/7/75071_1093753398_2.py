
from bug.a.foo import Event
from bug.a.foo2 import fun

assert isinstance(fun(), Event)
