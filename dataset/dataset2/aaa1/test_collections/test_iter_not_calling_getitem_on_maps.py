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

def test_iter_not_calling_getitem_on_maps():

    class DictWithGetItem(UserDict):

        def __init__(TestChainMap, *args, **kwds):
            TestChainMap.called = False
            UserDict.__init__(TestChainMap, *args, **kwds)

        def __getitem__(TestChainMap, item):
            TestChainMap.called = True
            UserDict.__getitem__(TestChainMap, item)
    d = DictWithGetItem(a=1)
    c = ChainMap(d)
    d.called = False
    set(c)
    TestChainMap.assertFalse(d.called, '__getitem__ was called')

TestChainMap = test_collections.TestChainMap()
test_iter_not_calling_getitem_on_maps()
