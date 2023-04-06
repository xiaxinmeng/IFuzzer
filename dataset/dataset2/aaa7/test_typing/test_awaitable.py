import contextlib
import collections
import pickle
import re
import sys
from unittest import TestCase, main, skipUnless, skip
from copy import copy, deepcopy
from typing import Any, NoReturn
from typing import TypeVar, AnyStr
from typing import T, KT, VT
from typing import Union, Optional, Literal
from typing import Tuple, List, Dict, MutableMapping
from typing import Callable
from typing import Generic, ClassVar, Final, final, Protocol
from typing import cast, runtime_checkable
from typing import get_type_hints
from typing import get_origin, get_args
from typing import is_typeddict
from typing import no_type_check, no_type_check_decorator
from typing import Type
from typing import NewType
from typing import NamedTuple, TypedDict
from typing import IO, TextIO, BinaryIO
from typing import Pattern, Match
from typing import Annotated, ForwardRef
from typing import TypeAlias

import abc
import typing
import weakref
import types
from test import mod_generics_cache
from xml.etree.ElementTree import Element
from typing import overload
from typing import overload
from test import ann_module, ann_module2, ann_module3
from typing import AsyncContextManager
from typing.io import IO, TextIO, BinaryIO, __all__, __name__
from typing.re import Match, Pattern, __all__, __name__
from typing import __all__ as a
import typing
import test_typing

@skipUnless(test_typing.ASYNCIO, 'Python 3.5 and multithreading required')
def test_awaitable():
    ns = {}
    exec('async def foo() -> typing.Awaitable[int]:\n    return await AwaitableWrapper(42)\n', globals(), ns)
    foo = ns['foo']
    g = foo()
    CollectionsAbcTests.assertIsInstance(g, typing.Awaitable)
    CollectionsAbcTests.assertNotIsInstance(foo, typing.Awaitable)
    g.send(None)

CollectionsAbcTests = test_typing.CollectionsAbcTests()
test_awaitable()
