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

def test_subtract():
    c = Counter(a=-5, b=0, c=5, d=10, e=15, g=40)
    c.subtract(a=1, b=2, c=-3, d=10, e=20, f=30, h=-50)
    TestCounter.assertEqual(c, Counter(a=-6, b=-2, c=8, d=0, e=-5, f=-30, g=40, h=50))
    c = Counter(a=-5, b=0, c=5, d=10, e=15, g=40)
    c.subtract(Counter(a=1, b=2, c=-3, d=10, e=20, f=30, h=-50))
    TestCounter.assertEqual(c, Counter(a=-6, b=-2, c=8, d=0, e=-5, f=-30, g=40, h=50))
    c = Counter('aaabbcd')
    c.subtract('aaaabbcce')
    TestCounter.assertEqual(c, Counter(a=-1, b=0, c=-1, d=1, e=-1))
    c = Counter()
    c.subtract(TestCounter=42)
    TestCounter.assertEqual(list(c.items()), [('TestCounter', -42)])
    c = Counter()
    c.subtract(iterable=42)
    TestCounter.assertEqual(list(c.items()), [('iterable', -42)])
    TestCounter.assertRaises(TypeError, Counter().subtract, 42)
    TestCounter.assertRaises(TypeError, Counter().subtract, {}, {})
    TestCounter.assertRaises(TypeError, Counter.subtract)

TestCounter = test_collections.TestCounter()
test_subtract()
