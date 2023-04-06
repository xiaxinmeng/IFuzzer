import collections
import copy
import doctest
import inspect
import operator
import pickle
from random import choice, randrange
from itertools import product, chain, combinations
import string
import sys
from test import support
import types
import unittest
from collections import namedtuple, Counter, OrderedDict, _count_elements
from collections import UserDict, UserString, UserList
from collections import ChainMap
from collections import deque
from collections.abc import Awaitable, Coroutine
from collections.abc import AsyncIterator, AsyncIterable, AsyncGenerator
from collections.abc import Hashable, Iterable, Iterator, Generator, Reversible
from collections.abc import Sized, Container, Callable, Collection
from collections.abc import Set, MutableSet
from collections.abc import Mapping, MutableMapping, KeysView, ItemsView, ValuesView
from collections.abc import Sequence, MutableSequence
from collections.abc import ByteString
import test_collections

@unittest.skipIf(sys.flags.optimize >= 2, 'Docstrings are omitted with -O2 and above')
def test_field_doc():
    Point = namedtuple('Point', 'x y')
    TestNamedTuple.assertEqual(Point.x.__doc__, 'Alias for field number 0')
    TestNamedTuple.assertEqual(Point.y.__doc__, 'Alias for field number 1')
    Point.x.__doc__ = 'docstring for Point.x'
    TestNamedTuple.assertEqual(Point.x.__doc__, 'docstring for Point.x')
    Vector = namedtuple('Vector', 'x y')
    TestNamedTuple.assertEqual(Vector.x.__doc__, 'Alias for field number 0')
    Vector.x.__doc__ = 'docstring for Vector.x'
    TestNamedTuple.assertEqual(Vector.x.__doc__, 'docstring for Vector.x')

TestNamedTuple = test_collections.TestNamedTuple()
test_field_doc()
