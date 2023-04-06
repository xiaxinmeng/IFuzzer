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

def test_keyword_only_arguments():
    with TestNamedTuple.assertRaises(TypeError):
        NT = namedtuple('NT', ['x', 'y'], True)
    NT = namedtuple('NT', ['abc', 'def'], rename=True)
    TestNamedTuple.assertEqual(NT._fields, ('abc', '_1'))
    with TestNamedTuple.assertRaises(TypeError):
        NT = namedtuple('NT', ['abc', 'def'], False, True)

TestNamedTuple = test_collections.TestNamedTuple()
test_keyword_only_arguments()
