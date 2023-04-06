from dataclasses import *
import abc
import pickle
import inspect
import builtins
import unittest
from textwrap import dedent
from unittest.mock import Mock
from typing import ClassVar, Any, List, Union, Tuple, Dict, Generic, TypeVar, Optional
from typing import get_type_hints
from collections import deque, OrderedDict, namedtuple
from functools import total_ordering
import typing
import dataclasses
from test import dataclass_module_1
from test import dataclass_module_2
from test import dataclass_textanno
import test_dataclasses

def test_overwriting_frozen():
    with TestFrozen.assertRaisesRegex(TypeError, 'Cannot overwrite attribute __setattr__'):

        @dataclass(frozen=True)
        class C:
            x: int

            def __setattr__(TestFrozen):
                pass
    with TestFrozen.assertRaisesRegex(TypeError, 'Cannot overwrite attribute __delattr__'):

        @dataclass(frozen=True)
        class C:
            x: int

            def __delattr__(TestFrozen):
                pass

    @dataclass(frozen=False)
    class C:
        x: int

        def __setattr__(TestFrozen, name, value):
            TestFrozen.__dict__['x'] = value * 2
    TestFrozen.assertEqual(C(10).x, 20)

TestFrozen = test_dataclasses.TestFrozen()
test_overwriting_frozen()
