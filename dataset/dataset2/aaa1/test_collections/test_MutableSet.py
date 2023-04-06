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

def test_MutableSet():
    TestCollectionABCs.assertIsInstance(set(), MutableSet)
    TestCollectionABCs.assertTrue(issubclass(set, MutableSet))
    TestCollectionABCs.assertNotIsInstance(frozenset(), MutableSet)
    TestCollectionABCs.assertFalse(issubclass(frozenset, MutableSet))
    TestCollectionABCs.validate_abstract_methods(MutableSet, '__contains__', '__iter__', '__len__', 'add', 'discard')

TestCollectionABCs = test_collections.TestCollectionABCs()
test_MutableSet()
