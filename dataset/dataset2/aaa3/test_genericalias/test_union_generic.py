import unittest
import pickle
from collections import defaultdict, deque, OrderedDict, Counter, UserDict, UserList
from collections.abc import *
from concurrent.futures import Future
from concurrent.futures.thread import _WorkItem
from contextlib import AbstractContextManager, AbstractAsyncContextManager
from contextvars import ContextVar, Token
from dataclasses import Field
from functools import partial, partialmethod, cached_property
from mailbox import Mailbox, _PartialFile
import ctypes
from difflib import SequenceMatcher
from filecmp import dircmp
from fileinput import FileInput
from itertools import chain
from http.cookies import Morsel
from multiprocessing.managers import ValueProxy
from multiprocessing.pool import ApplyResult
from multiprocessing.shared_memory import ShareableList
from multiprocessing.queues import SimpleQueue as MPSimpleQueue
from os import DirEntry
from re import Pattern, Match
from types import GenericAlias, MappingProxyType, AsyncGeneratorType
from tempfile import TemporaryDirectory, SpooledTemporaryFile
from urllib.parse import SplitResult, ParseResult
from unittest.case import _AssertRaisesContext
from queue import Queue, SimpleQueue
from weakref import WeakSet, ReferenceType, ref
import typing
from typing import TypeVar
import types
from typing import List, Dict, Callable
from typing import List, Dict, Union, Callable
import test_genericalias

def test_union_generic():
    a = typing.Union[list[test_genericalias.T], tuple[test_genericalias.T, ...]]
    BaseTest.assertEqual(a.__args__, (list[test_genericalias.T], tuple[test_genericalias.T, ...]))
    BaseTest.assertEqual(a.__parameters__, (test_genericalias.T,))

BaseTest = test_genericalias.BaseTest()
test_union_generic()
