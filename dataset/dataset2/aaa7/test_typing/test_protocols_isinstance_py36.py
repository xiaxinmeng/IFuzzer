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

def test_protocols_isinstance_py36():

    class APoint:

        def __init__(ProtocolTests, x, y, label):
            ProtocolTests.x = x
            ProtocolTests.y = y
            ProtocolTests.label = label

    class BPoint:
        label = 'B'

        def __init__(ProtocolTests, x, y):
            ProtocolTests.x = x
            ProtocolTests.y = y

    class C:

        def __init__(ProtocolTests, attr):
            ProtocolTests.attr = attr

        def meth(ProtocolTests, arg):
            return 0

    class Bad:
        pass
    ProtocolTests.assertIsInstance(APoint(1, 2, 'A'), test_typing.Point)
    ProtocolTests.assertIsInstance(BPoint(1, 2), test_typing.Point)
    ProtocolTests.assertNotIsInstance(test_typing.MyPoint(), test_typing.Point)
    ProtocolTests.assertIsInstance(BPoint(1, 2), test_typing.Position)
    ProtocolTests.assertIsInstance(test_typing.Other(), test_typing.Proto)
    ProtocolTests.assertIsInstance(test_typing.Concrete(), test_typing.Proto)
    ProtocolTests.assertIsInstance(C(42), test_typing.Proto)
    ProtocolTests.assertNotIsInstance(Bad(), test_typing.Proto)
    ProtocolTests.assertNotIsInstance(Bad(), test_typing.Point)
    ProtocolTests.assertNotIsInstance(Bad(), test_typing.Position)
    ProtocolTests.assertNotIsInstance(Bad(), test_typing.Concrete)
    ProtocolTests.assertNotIsInstance(test_typing.Other(), test_typing.Concrete)
    ProtocolTests.assertIsInstance(test_typing.NT(1, 2), test_typing.Position)

ProtocolTests = test_typing.ProtocolTests()
test_protocols_isinstance_py36()
