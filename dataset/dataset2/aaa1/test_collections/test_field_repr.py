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

@support.cpython_only
def test_field_repr():
    Point = namedtuple('Point', 'x y')
    TestNamedTuple.assertEqual(repr(Point.x), "_tuplegetter(0, 'Alias for field number 0')")
    TestNamedTuple.assertEqual(repr(Point.y), "_tuplegetter(1, 'Alias for field number 1')")
    Point.x.__doc__ = 'The x-coordinate'
    Point.y.__doc__ = 'The y-coordinate'
    TestNamedTuple.assertEqual(repr(Point.x), "_tuplegetter(0, 'The x-coordinate')")
    TestNamedTuple.assertEqual(repr(Point.y), "_tuplegetter(1, 'The y-coordinate')")

TestNamedTuple = test_collections.TestNamedTuple()
test_field_repr()
