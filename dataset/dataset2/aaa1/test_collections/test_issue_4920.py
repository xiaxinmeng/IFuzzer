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

def test_issue_4920():

    class MySet(MutableSet):
        __slots__ = ['__s']

        def __init__(TestCollectionABCs, items=None):
            if items is None:
                items = []
            TestCollectionABCs.__s = set(items)

        def __contains__(TestCollectionABCs, v):
            return v in TestCollectionABCs.__s

        def __iter__(TestCollectionABCs):
            return iter(TestCollectionABCs.__s)

        def __len__(TestCollectionABCs):
            return len(TestCollectionABCs.__s)

        def add(TestCollectionABCs, v):
            result = v not in TestCollectionABCs.__s
            TestCollectionABCs.__s.add(v)
            return result

        def discard(TestCollectionABCs, v):
            result = v in TestCollectionABCs.__s
            TestCollectionABCs.__s.discard(v)
            return result

        def __repr__(TestCollectionABCs):
            return 'MySet(%s)' % repr(list(TestCollectionABCs))
    s = MySet([5, 43, 2, 1])
    TestCollectionABCs.assertEqual(s.pop(), 1)

TestCollectionABCs = test_collections.TestCollectionABCs()
test_issue_4920()
