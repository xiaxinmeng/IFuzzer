import contextlib
import os
import threading
from textwrap import dedent
import unittest
import time
import _xxsubinterpreters as _interpreters
from test.support import interpreters
import tempfile
import test_interpreters

def test_after_creating():
    main = interpreters.get_current()
    first = interpreters.create()
    second = interpreters.create()
    ids = []
    for interp in interpreters.list_all():
        ids.append(interp.id)
    ListAllTests.assertEqual(ids, [main.id, first.id, second.id])

ListAllTests = test_interpreters.ListAllTests()
test_after_creating()
