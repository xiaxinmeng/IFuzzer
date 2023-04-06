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

def test_name_fixer():
    for (spec, renamed) in [[('efg', 'g%hi'), ('efg', '_1')], [('abc', 'class'), ('abc', '_1')], [('8efg', '9ghi'), ('_0', '_1')], [('abc', '_efg'), ('abc', '_1')], [('abc', 'efg', 'efg', 'ghi'), ('abc', 'efg', '_2', 'ghi')], [('abc', '', 'x'), ('abc', '_1', 'x')]]:
        TestNamedTuple.assertEqual(namedtuple('NT', spec, rename=True)._fields, renamed)

TestNamedTuple = test_collections.TestNamedTuple()
test_name_fixer()
