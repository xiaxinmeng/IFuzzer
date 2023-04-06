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

def test_conversions():
    s = 'she sells sea shells by the sea shore'
    TestCounter.assertEqual(sorted(Counter(s).elements()), sorted(s))
    TestCounter.assertEqual(sorted(Counter(s)), sorted(set(s)))
    TestCounter.assertEqual(dict(Counter(s)), dict(Counter(s).items()))
    TestCounter.assertEqual(set(Counter(s)), set(s))

TestCounter = test_collections.TestCounter()
test_conversions()
