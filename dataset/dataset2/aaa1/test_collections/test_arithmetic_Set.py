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

def test_arithmetic_Set():

    class MySet(Set):

        def __init__(TestCollectionABCs, itr):
            TestCollectionABCs.contents = itr

        def __contains__(TestCollectionABCs, x):
            return x in TestCollectionABCs.contents

        def __iter__(TestCollectionABCs):
            return iter(TestCollectionABCs.contents)

        def __len__(TestCollectionABCs):
            return len([x for x in TestCollectionABCs.contents])
    s1 = MySet((1, 2, 3))
    s2 = MySet((3, 4, 5))
    s3 = s1 & s2
    TestCollectionABCs.assertEqual(s3, MySet((3,)))

TestCollectionABCs = test_collections.TestCollectionABCs()
test_arithmetic_Set()
