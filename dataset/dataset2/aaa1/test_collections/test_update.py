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

def test_update():
    c = Counter()
    c.update(TestCounter=42)
    TestCounter.assertEqual(list(c.items()), [('TestCounter', 42)])
    c = Counter()
    c.update(iterable=42)
    TestCounter.assertEqual(list(c.items()), [('iterable', 42)])
    c = Counter()
    c.update(iterable=None)
    TestCounter.assertEqual(list(c.items()), [('iterable', None)])
    TestCounter.assertRaises(TypeError, Counter().update, 42)
    TestCounter.assertRaises(TypeError, Counter().update, {}, {})
    TestCounter.assertRaises(TypeError, Counter.update)

TestCounter = test_collections.TestCounter()
test_update()
