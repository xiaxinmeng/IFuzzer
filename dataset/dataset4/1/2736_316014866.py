
# x.py
from collections import namedtuple
nts = [namedtuple(f"Foo{i}", "foo,bar,baz") for i in range(10000)]
